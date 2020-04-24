from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser) :
    profile = models.ImageField(upload_to='profile')
    address = models.CharField(max_length=150)
