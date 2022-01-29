"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django import views
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, PasswordChangeView

# from tinyapp.views import UserRegistrationView, UrlListView, CreateUrl, url_redirect, UrlDeleteView, UrlEditView, loginPage, logoutPage

from tinyapp import views

urlpatterns = [
    path('', lambda req: redirect('login')),
    path('admin/', admin.site.urls),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('urls/', login_required(views.UrlListView.as_view(),
         login_url='login'), name='urls'),
    path('urls/new/', views.CreateUrl, name="create_url"),
    path('u/<str:shortUrl>', views.url_redirect, name='url-redirect'),
    path('urls/<int:pk>', views.UrlDetailView.as_view(), name='url-detail'),
    path('urls/delete/<int:pk>', login_required(views.UrlDeleteView.as_view(),
         login_url='login'), name='url-delete'),
    path('urls/edit/<int:pk>', login_required(views.UrlEditView.as_view(),
         login_url='login'), name='url-edit'),
    path('login/', views.loginPage,  name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('userlist/', login_required(views.UserListView.as_view(),
         login_url='login'), name='user-list')
]
