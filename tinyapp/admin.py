from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Url

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Url)
admin.site.site_header = 'TinyApp Administration'
