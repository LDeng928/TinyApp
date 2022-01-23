from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Url(models.Model):
    shortUrl = models.URLField(max_length=200)
    longUrl = models.URLField(max_length=250)
    dateCreated = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE,)
