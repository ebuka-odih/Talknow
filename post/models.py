from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Post(models.Model):
   title = models.CharField(max_length=100)
   overview = models.TextField()
   timestamp = models.DateTimeField(auto_now_add=True)
   comment_count = models.IntegerField(default = 0)
   view_count = models.IntegerField(default = 0)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   thumbnail = models.ImageField(upload_to="thumbnail")
   tags = TaggableManager()
   
   
   def __str__(self):
        return self.title



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.post) 

