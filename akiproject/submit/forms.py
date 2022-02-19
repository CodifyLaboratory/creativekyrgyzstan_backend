from django import forms
from .models import Submit

class CreateSubmit(forms.ModelForm):
    class Meta:
        model = Submit
        fields = '__all__'