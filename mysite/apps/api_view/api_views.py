from myapp.models import Post,User
from rest_framework.response import Response
from rest_framework.views import APIView
from myapp.serializers import PostSerializer,UserSerializer,UpdateUserSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from myapp import serializers
from django.core.mail import  EmailMessage
from django.conf import settings
from django.template.loader import get_template 
from django.template.loader import render_to_string
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.contrib.auth import logout

class UserLoginAPI(generics.CreateAPIView):
    # import pdb; pdb.set_trace()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    
    def post(self, request, *args, **kwargs):    
        # import pdb; pdb.set_trace()    
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        Token.objects.filter(user=user).delete()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,"message": "Login Successfully",'user':username},
                    status=HTTP_200_OK)


class UserLogoutAPI(generics.DestroyAPIView,UserLoginAPI):
    permission_classes = (IsAuthenticated,) 

    def get(self, request, format=None):
        Token.objects.filter(user=request.user).delete()       
        logout(request)
        return Response({"message": "logout Successfully","code": 204,})


class UpdateProfileView(generics.RetrieveUpdateAPIView):

    # import pdb; pdb.set_trace()
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer


class DeleteAPIView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def delete(self, request, *args, **kwargs):
        Token.objects.filter(user=request.user).delete()
        user=self.request.user
        user.delete()
        return Response({"result":"user delete"})


class PostListAPIView(generics.ListCreateAPIView):

    queryset = Post.objects.all() 
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # import pdb; pdb.set_trace()
        serializer.save(author=self.request.user)
        user = User.objects.get(id=self.request.user.id)
        user_email=user.email
        from_email = settings.EMAIL_HOST_USER
        
        context = {
            'user': user,
            'user_email':user_email,        
        }
        html_template = get_template('myapp/message.html').render(context)
        # html_message = render_to_string(html_template, { 'context': context, })
        msg = EmailMessage('Subject aapke hissab de skte ho..... !',
                  html_template,
                   from_email, 
                  [user_email],
                  )

        msg.content_subtype ="html"
        msg.send()
        print("Mail successfully sent")


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


    









    # def update(self, request, *args, **kwargs):
    #     Token.objects.filter(user=request.user)
    #     user=self.request.user
         
    #     return Response({"result":"user update"})
        
    # def put(self, request, user_id, format=None):
    #     import pdb; pdb.set_trace()
    #     user = User.objects.get(userid=user_id)
    #     Token.objects.filter(user=request.user)
    #     serializer = UserSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     # return self.update(request, *args, **kwargs)
    #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

# class UserProfileUpdateView(generics.UpdateAPIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = ((IsAuthenticated,))
#     serializer_class = UserProfileSerializer
#     def get_object(self):
#         return User.objects.get(user=self.request.user)

# class DeleteAPIView(generics.DestroyAPIView):
#     queryset = User.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = serializers.UserSerializer
#     lookup_field = 'pk'

#     def destroy(self, request, pk=None, *args, **kwargs):
#         instance = self.get_object()
#         # you custom logic #
#         return super(DeletePostViewSet, self).destroy(request, pk, *args, **kwargs)
#         return JsonResponse({"message": "logout Successfully","code": 201,})





# class PostListAPIView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


