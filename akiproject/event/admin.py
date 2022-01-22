from django.contrib import admin
from django.forms import inlineformset_factory

# Register your models here.

from .models import Event, EventImages

# admin.site.register(Event)
# admin.site.register(EventImages)

class EventImagesAdmin(admin.StackedInline):
    model = EventImages

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventImagesAdmin]

    class Meta:
        model = Event