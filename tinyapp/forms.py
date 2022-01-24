from dataclasses import field, fields
from pyexpat import model
from statistics import mode
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User, Url
from django import forms


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']


class UrlCreateForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ["longUrl", "user_id"]
        widgets = {
            'longUrl': forms.TextInput(attrs={'placeholder': 'http://'})
        }
