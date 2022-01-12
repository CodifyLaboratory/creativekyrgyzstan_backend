from django.shortcuts import render
from .models import Members, RulesAndPolitics
from django.conf import settings

# Create your views here.

def members_show(request):
    rules_and_politics = RulesAndPolitics.objects.get()
    members = Members.objects.all()
    context = {'members':members,
                'rules_and_politics':rules_and_politics,
                'media_url':settings.MEDIA_URL,}
    return render (request, 'association_member.html', context)