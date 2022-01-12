from rest_framework import serializers
from mainpage.models import MainPage

class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'