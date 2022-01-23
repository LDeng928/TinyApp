from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']
