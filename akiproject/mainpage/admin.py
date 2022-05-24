from django.contrib import admin

# Register your models here.

from .models import MainPage, Footer

admin.site.register(MainPage)
admin.site.register(Footer)