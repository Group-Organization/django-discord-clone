from django.forms import ModelForm
from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
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
            'dob': DateInput(),
        }
