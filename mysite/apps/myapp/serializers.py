from rest_framework import serializers
from .models import Post,User

class PostSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Post
		fields = ('author','id','title', 'description', 'pic', ) 


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username','password', 'posts']


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','username','email','first_name','last_name']

    # def create(self,validated_data):
    #     user=User.objects.create_user(**validated_data)
    #     User.objects.create(user=user)
    #     user.save()
    #     return user

    # def update(self,instance,validated_data):
    #     user=User.objects.update(**validated_data)
    #     UserDetails.objects.update(user=user)
    #     user.save()
    #     return user