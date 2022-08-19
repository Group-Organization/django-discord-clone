from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('email address' ,unique=True)
    username = models.CharField(max_length=30, unique=True)
    tag = models.IntegerField(default=0000)
    bio = models.TextField(max_length=512, blank=True)
    status = models.CharField(max_length=64, blank=True)
    dob = models.DateField(blank=True)
    profile_picture = models.ImageField(blank=True, default='default.png')
    friend = models.ManyToManyField('User', related_name='friends', blank=True)
    blocked_users = models.ManyToManyField('User', related_name='blocked', blank=True)
    servers = models.ManyToManyField('app.Server', related_name='servers', blank=True)
    created = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.username
