from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import UserManager


class Post(models.Model):
    is_good=models.BooleanField()
    title = models.CharField(max_length=255,default=None)

    description = models.TextField(max_length=5000 ,default=None)

    pic = models.ImageField(upload_to='images/',height_field=None, width_field=None ,blank=True,null=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)
    date_posted =  models.DateTimeField(default=timezone.now)

    likes = models.ManyToManyField(User, related_name='user_likes', blank=True)
    

    objects = UserManager()
    
    def total_likes(self):
        return self.likes.count()

    def publish(self):
        self.date_posted = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.content


# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
#     content = models.TextField(max_length=5000)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     date_posted =  models.DateTimeField(default=timezone.now)
    
#     def __str__(self):
#         return self.content

    # def get_absolute_url(self):
    #     return reverse('myapp:detail')

    # def get_absolute_url(self):


# class comment(models.Model):
    
#     comments = models.ForeignKey(Post, related_name='user_comment',on_delete=models.CASCADE, blank=True)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     content = models.TextField(max_length=5000 ,default=None)
#     date_posted =  models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.author 

#     def publish(self):
#         self.date_posted = timezone.now()
#         self.save()

    