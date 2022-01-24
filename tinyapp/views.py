from ast import alias
from dataclasses import fields
from pyexpat import model
from statistics import mode
from typing import List
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.template import context
from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.edit import FormView
from .models import User, Url
from .forms import UserRegisterForm, UrlCreateForm
import string
import random

# Create your views here.


class UserRegistrationView(CreateView):
    form_class = UserRegisterForm
    success_url = "/register"
    template_name = "register.html"


class UrlListView(ListView):
    model = Url
    context_object_name = 'urls'
    template_name = "urls_index.html"
    success_url = "/urls"

# Create TinyURL form


class UrlCreateView(CreateView):
    template_name = "urls_new.html"
    form_class = UrlCreateForm
    # def get(self, request, *args, **kwargs):
    #     context = {'form': UrlCreateForm()}
    #     return render(request, 'urls_new.html', context)

    def random_string():
        string_size = 6
        ran_string = ''
        return ran_string.join(random.choices(string.ascii_letters+string.digits, k=string_size))

    def form_valid(self, form):
        user = User.objects.get()
        form.instance.user = user
        form.instance.shortUrl = self.random_string()
        return super().form_valid(form)


def random_string():
    string_size = 6
    ran_string = ''
    return ran_string.join(random.choices(string.ascii_letters+string.digits, k=string_size))


# Functional way to create form
def CreateUrl(request):
    form = UrlCreateForm

    if request.method == 'POST':
        # print('Printing Post', request.POST)
        URL = request.POST["longUrl"]
        shortUrl = request.POST.get("shortUrl", None)
        if not shortUrl:
            shortUrl = random_string()

            Url.objects.create(user_id=request.user,
                               longUrl=URL, shortUrl=shortUrl).save()
            return redirect("/urls")

    context = {'form': form}
    return render(request, 'urls_new.html', context)
