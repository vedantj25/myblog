from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
 title = models.CharField(max_length=255)
 title_tag = models.CharField(max_length=255)
 author = models.ForeignKey(User, on_delete=models.CASCADE)
 body = RichTextField(blank=True, null=True)
 snippet = models.CharField(max_length=255)
 created_date = models.DateTimeField(auto_now_add=True)
 
 def __str__(self):
  return self.title + ' | ' + str(self.author)
 
 def get_absolute_url(self):
  return reverse('post-detail', args=(str(self.id)))

class Comment(models.Model):
 post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
 name = models.CharField(max_length=255)
 email = models.EmailField()
 body = models.TextField()
 date_added = models.DateTimeField(auto_now_add=True)
 
 def __str__(self):
  return '%s - %s' % (self.post.title, self.name)