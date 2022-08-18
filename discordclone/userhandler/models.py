from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    tag = models.CharField(max_length=4)
    bio = models.TextField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=128, unique=True)
    profile_picture = models.ImageField(
        default='default.png',)
#     friends = models.ManyToManyField(User, related_name='Friends', blank=True)
#     servers = models.ManyToManyField(
#         Server, related_name='Servers', blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
