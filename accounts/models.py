from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
# Create your models here.

class MyUser(AbstractUser) :
    profile = models.ImageField(upload_to='profile')
    address = models.CharField(max_length=150)

    # def delete(self, *args, **kwargs):
    #     os.remove(os.path.join(settings.MEDIA_ROOT,'profile',self.profile.path))
    #     super(MyUser,self).delete(*args, **kwargs)