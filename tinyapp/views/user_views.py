from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.template import context
from django.views.generic import CreateView
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
