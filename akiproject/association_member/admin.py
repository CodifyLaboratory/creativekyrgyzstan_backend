from dataclasses import fields
from django.contrib import admin
from .models import RulesAndPolitics, Members
from submit.models import Submit
from django import forms

# class SubmitInline(admin.StackedInline):
#     model = Submit



class MembersForm(forms.ModelForm):

    class Meta:
        model = Members
        fields = '__all__'


admin.site.register(RulesAndPolitics)


class MembersAdmin(admin.ModelAdmin):
    # list_display = ('submit.full_name', )
    list_select_related = (
        'submit',
    )
    
    form = MembersForm

admin.site.register(Members, MembersAdmin)
