import akiproject.translation
from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from django.utils.safestring import mark_safe


# Register your models here.

from .models import Submit

@admin.register(Submit)
class SubmitAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'full_name', 'company_email', 'company_phone')
    # readonly_fields = ('get_image',)
    list_display_links = ['company_name']
    save_on_top = True

    # def get_image(self, obj):
    #     return mark_safe(f'<img src={obj.company_logo.url} width="50" height="50">')

    # get_image.short_description = 'Логотип'    
