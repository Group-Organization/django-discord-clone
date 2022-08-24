import uuid
from django.db import models
from userhandler.models import User

# Create your models here.


class Server(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256, blank=True)
    owner = models.ForeignKey('userhandler.User', on_delete=models.CASCADE)
    participants = models.ManyToManyField(
        'userhandler.User', related_name='participants')
    roles = models.ManyToManyField('Role', related_name='roles', blank=True)
    voice_channels = models.ManyToManyField(
        'VoiceChannel', related_name='voice_channels', blank=True)
    text_channels = models.ManyToManyField(
        'TextChannel', related_name='text_channels', blank=True)
    messages = models.ManyToManyField(
        'Message', related_name='messages', blank=True)
    logo = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=30)
    server = models.ForeignKey('Server', on_delete=models.CharField)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Message(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(
        'userhandler.User', on_delete=models.SET_NULL, null=True)
    message = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class TextChannel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64, null=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, null=True)
    participants = models.ManyToManyField(
        'userhandler.User', related_name='ChannelParticipants', blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class VoiceChannel(TextChannel):
    pass


class ServerMessage(Message):
    channel = models.ForeignKey(TextChannel, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
