from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

