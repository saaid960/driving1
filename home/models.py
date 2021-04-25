from django.db import models
from embed_video.fields import EmbedVideoField


class messages(models.Model):
    name = models.TextField(max_length=30)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class TodoItem(models.Model):
    content = models.TextField()
    
    def __str__(self):
        return self.content

class VIDEO(models.Model):
    video = EmbedVideoField()  # same like models.URLField()

class contact(models.Model):
    name = models.TextField(max_length=30)
    email = models.EmailField()
    message = models.CharField(max_length=10)
