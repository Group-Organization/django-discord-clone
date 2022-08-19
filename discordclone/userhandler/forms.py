from django.forms import ModelForm
from django import forms
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture', 'dob']
        profile_picture = forms.ImageField()
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'eg: JohnDoe',
                'id': 'username',
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'eg: JohnDoe@gmail.com',
                'id': 'email',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': '•••••••',
                'id': 'password',
            }), 
            'bio': forms.Textarea(attrs={
                'placeholder': 'Introduce yourself..',
                'id': 'bio',
            }),
        }
