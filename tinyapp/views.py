from dataclasses import fields
from pyexpat import model
from statistics import mode
from typing import List
from django.forms import ModelForm
from django.shortcuts import render
from django.template import context
from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.edit import FormView
from .models import User, Url
from .forms import UserRegisterForm, UrlCreateForm

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
    success_url = "/urls"

# Create TinyURL form


class UrlCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': UrlCreateForm()}
        return render(request, 'urls_new.html', context)
