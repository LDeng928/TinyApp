from pyexpat import model
from typing import List
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import User, Url
from .forms import UserRegisterForm

# Create your views here.


class UserRegistrationView(CreateView):
    form_class = UserRegisterForm
    success_url = "/register"
    template_name = "register.html"


class UrlListView(ListView):
    model = Url
    queryset = [{'shortUrl': 'b2xVn2',
                 'longUrl': 'https://www.google.com', 'user_id': 2}]
    context_object_name = 'urls'
    template_name = "urls_index.html"
