from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile/',blank=True,null=True)
    stack = models.CharField(max_length=50,null=True,blank=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    
