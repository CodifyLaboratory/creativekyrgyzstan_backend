from django.contrib import admin

# Register your models here.

from .models import Event, EventImages



admin.site.register(Event)
admin.site.register(EventImages)