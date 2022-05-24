from django.shortcuts import render
from .models import MainPage
from django.conf import settings

# Create your views here.

def mainpage(request):
    index = MainPage.objects.get()
    context = {'index':index , 'media_url':settings.MEDIA_URL,}
    return render (request, 'index.html', context)