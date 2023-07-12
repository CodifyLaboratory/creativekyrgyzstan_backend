from rest_framework import serializers
from mainpage.models import MainPage, Footer

class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'