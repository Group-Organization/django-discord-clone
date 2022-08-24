from django.forms import ModelForm
from django import forms
from .models import *


class ServerMessageForm(ModelForm):
    class Meta:
        model = ServerMessage
        fields = ['message']
