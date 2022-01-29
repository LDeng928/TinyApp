from ast import Delete, alias
from dataclasses import fields
from pyexpat import model
from statistics import mode
from typing import List
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.template import context
from django.views.generic import CreateView, ListView, TemplateView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from .models import User, Url
from .forms import UserRegisterForm, UrlCreateForm
import string
import random

# Create your views here.


class UserRegistrationView(CreateView):
    form_class = UserRegisterForm
    success_url = "/register"
    template_name = "register.html"


@login_required(login_url='login')
class UrlListView(ListView):
    model = Url
    context_object_name = 'urls'
    template_name = "urls_index.html"
    success_url = "/urls"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.session.get('myCookie'))
        return context

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


@login_required(login_url='login')
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

# URL detail view


# class UrlDetailView(DetailView):
#     model = Url
#     template_name = "url_detail.html"

@login_required(login_url='login')
def url_redirect(request, shortUrl):
    obj = Url.objects.get(shortUrl=shortUrl)
    URL = obj.longUrl
    return redirect(URL)


# URL Delete view
class UrlDeleteView(DeleteView):
    model = Url
    success_url = "/urls"

# URL Update view


class UrlEditView(UpdateView):
    model = Url
    fields = ['longUrl']
    template_name = 'url_detail.html'

    def get_success_url(self):
        return '/urls'

# User Login view


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('urls')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                login(request, user)
                return redirect('urls')
            else:
                messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)

# User logout view


def logoutPage(request):
    logout(request)
    return redirect('login')
