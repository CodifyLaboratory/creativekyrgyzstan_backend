from django.shortcuts import render
from .models import Event
from django.conf import settings

# Create your views here.

def show_event(request):
    event = Event.objects.all()
    context = {'event':event, 'media_url':settings.MEDIA_URL,}
    return render (request, 'event.html', context)