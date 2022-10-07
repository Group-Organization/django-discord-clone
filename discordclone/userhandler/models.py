from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    username = models.CharField(max_length=30)
    bio = models.TextField(max_length=512, blank=True)
    tag = models.IntegerField(default=0000)
    status = models.CharField(max_length=64, blank=True)
    dob = models.DateField(blank=True)
    profile_picture = models.ImageField(
        blank=True, upload_to='', default='default.png')
    friends = models.ManyToManyField(
        'User', related_name='user_friends', blank=True)
    blocked_users = models.ManyToManyField(
        'User', related_name='blocked', blank=True)
    servers = models.ManyToManyField(
        'app.Server', related_name='servers', blank=True)
    pending_users = models.ManyToManyField(
        'User', related_name='pending', blank=True)
    created = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'dob']

    def __str__(self):
        return f'{self.username}#{str(self.tag)}'
