from django.urls import path
from .import views
# from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'myapp'  
urlpatterns = [
    path('', views.index.as_view(),name='about'),
    path('login/',auth_views.LoginView.as_view(template_name = 'myapp/login.html',redirect_authenticated_user = True),name='login'),
    path('signup/', views.SignUpView.as_view(),name='signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'myapp/logout.html'), name='logout'),
    path('profile/<int:pk>/',views.ProfileView.as_view(),name='profile'),
    path('home/update/<int:pk>/', views.UserUpdate.as_view(),name='userupdate'),
    path('upload/',views.CreatePostView.as_view(),name='upload'),
    path('home/',views.PostList.as_view(),name='home'),
    path('delete/<int:pk>/', views.PostDelete.as_view(),name='delete'),
    path('home/update2/<int:pk>/',views.PostUpdate.as_view(),name='postupdate'),
    path('home/detail/<int:pk>/', views.PostDetail.as_view(),name='detail'),
    path('author/',views.UserPostListView.as_view(),name="userpost"),
    path('like/<int:pk>/', views.like_post, name="like_post"),
    path('comment/<int:pk>/', views.add_comment, name="comment"),

    # path('email/', views.bhej_email, name="email"),
]



