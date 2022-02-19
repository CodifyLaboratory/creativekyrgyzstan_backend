from django.shortcuts import render
from django.forms import modelformset_factory
from django.conf import settings
from .forms import CreateSubmit

# Create your views here.

def submit(request):
    application = CreateSubmit()
    context = {
        'application':application
    }
    return render (request, 'submit.html', context)