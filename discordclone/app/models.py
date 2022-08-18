from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class Users(AbstractUser):
    email = models.EmailField('email address' ,unique=True)
    username = models.CharField(max_length=30, unique=True)
    tag = models.IntegerField(default=0000)
    bio = models.TextField(max_length=512, blank=True)
    status = models.CharField(max_length=64, blank=True)
    dob = models.DateTimeField(null=True)
    profile_picture = models.ImageField(blank=True)
    friend = models.ManyToManyField('Users', related_name='friends', blank=True)
    blocked_users = models.ManyToManyField('Users', related_name='blocked', blank=True)
    servers = models.ManyToManyField('Server', related_name='servers', blank=True)
    created = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.username

class Server(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256, blank=True)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Users, related_name='participants')
    roles = models.ManyToManyField('Role', related_name='roles', blank=True)
    voice_channels = models.ManyToManyField('VoiceChannel', related_name='voice_channels', blank=True)
    text_channels = models.ManyToManyField('TextChannel', related_name='text_channels', blank=True)
    messages = models.ManyToManyField('Message', related_name='messages', blank=True)
    logo = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length=30)
    server = models.ForeignKey('Server', on_delete=models.CharField)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    message = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class ServerMessage(Message):
    channel = models.ForeignKey('TextChannel', on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)


class TextChannel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=64, null=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, null=True)
    participants = models.ManyToManyField(Users, related_name='ChannelParticipants', blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class VoiceChannel(TextChannel):
    pass