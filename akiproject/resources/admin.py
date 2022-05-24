from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.

from .models import Recommendation, CreativeProject, FormalRegistrations, HeaderText

admin.site.register(HeaderText)

class RecommendationAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    text_kg = forms.CharField(widget=CKEditorUploadingWidget())
    text_en = forms.CharField(widget=CKEditorUploadingWidget())


    class Meta:
        model = Recommendation
        fields = '__all__'

class CreativeProjectAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    text_kg = forms.CharField(widget=CKEditorUploadingWidget())
    text_en = forms.CharField(widget=CKEditorUploadingWidget())


    class Meta:
        model = CreativeProject
        fields = '__all__'

class FormalRegistrationsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    text_kg = forms.CharField(widget=CKEditorUploadingWidget())
    text_en = forms.CharField(widget=CKEditorUploadingWidget())


    class Meta:
        model = FormalRegistrations
        fields = '__all__'

# admin.site.register(Recommendation)
@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    form = RecommendationAdminForm
    
# admin.site.register(CreativeProject)
@admin.register(CreativeProject)
class CreativeProjectAdmin(admin.ModelAdmin):
    form = CreativeProjectAdminForm

# admin.site.register(FormalRegistrations)
@admin.register(FormalRegistrations)
class FormalRegistrationsAdmin(admin.ModelAdmin):
    form = FormalRegistrationsAdminForm

