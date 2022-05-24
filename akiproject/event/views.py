from django.shortcuts import render
from django.forms import modelformset_factory
from .models import Event, EventImages
from django.conf import settings

# Create your views here.

# def show_event(request):
#     event = Event.objects.all()
#     images = EventImages.objects.all()
#     context = {'event':event, 'media_url':settings.MEDIA_URL, 'images':images}
#     return render (request, 'event.html', context)