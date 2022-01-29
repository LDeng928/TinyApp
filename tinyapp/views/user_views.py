from pyexpat import model
from typing import List
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.template import context
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

from tinyapp.models import User
from ..forms import UserRegisterForm


# Create your views here.


class UserRegistrationView(CreateView):
    form_class = UserRegisterForm
    success_url = "/register"
    template_name = "register.html"

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


# Admin User List View
class UserListView(PermissionRequiredMixin, ListView):
    permission_required = 'tinyapp.view_user'
    model = User
    context_object_name = 'users'
    template_name = "admin.html"
    success_url = "/userlist"

    # def get_queryset(self):
    #     user = self.request.user
    #     if(user.has_perms('tinyapp.view_user')):
    #         return User.objects.all()
    #     return User.objects.none()
