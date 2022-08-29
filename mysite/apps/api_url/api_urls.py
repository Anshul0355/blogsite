from django.urls import path
from api_view.api_views import PostListAPIView,PostDetailAPIView,UserLoginAPI,UserLogoutAPI,UpdateProfileView,DeleteAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Mysite Project API",
      default_version='v1',
      description="User description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
	path('', PostListAPIView.as_view()),
	path('login/', UserLoginAPI.as_view(), name='login'),
	path('logout/', UserLogoutAPI.as_view(), name='logout'),
	path('update/<int:pk>', UpdateProfileView.as_view(), name='update'),
	path('delete/', DeleteAPIView.as_view(), name='delete'),
	path('detail/<int:pk>', PostDetailAPIView.as_view()),
	path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]	