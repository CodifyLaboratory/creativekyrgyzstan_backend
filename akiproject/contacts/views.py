from django.shortcuts import render
from .models import Contact
from django.conf import settings

# Create your views here.

def contact(request):
    contact = Contact.objects.get()
    context = {'contact':contact, 'media_url':settings.MEDIA_URL,}
    return render (request, 'contact.html', context)