from django.contrib import admin

# Register your models here.

from .models import RulesAndPolitics, Members

admin.site.register(RulesAndPolitics)
admin.site.register(Members)