from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.template import context
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from ..models import User, Url
from ..forms import UrlCreateForm
import string
import random


class UrlListView(ListView):
    model = Url
    context_object_name = 'urls'
    template_name = "urls_index.html"
    success_url = "/urls"

    def get_queryset(self):
        user = self.request.user.id
        print(user)
        return Url.objects.filter(user_id=user)


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


def url_redirect(request, shortUrl):
    obj = Url.objects.get(shortUrl=shortUrl)
    URL = obj.longUrl
    return redirect(URL)


# URL detail view - (not in use)
class UrlDetailView(DetailView):
    model = Url
    template_name = "url_detail.html"


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

    # Raise exception if the current user is trying to access another user's url edit view
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.user_id != self.request.user.id:
            raise PermissionDenied
        return super(UrlEditView, self).get(request, *args, **kwargs)
