from rest_framework import serializers
from resources.models import Recommendation, FormalRegistrations, CreativeProject, HeaderText

class HeaderTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderText
        fields = '__all__'

class RecommendationSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_photo_url')
        
    class Meta:
        model = Recommendation
        fields = ('id','name','description','text','name_kg','description_kg','text_kg',
        'name_en','description_en','text_en','post_date', 'image')  
    
    def get_photo_url(self, event):
        request = self.context.get('request')
        try:
            image_url = event.image.url
            return request.build_absolute_uri('https://creative.kg' + image_url)
        except:
            return None

class FormalRegistrationsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = FormalRegistrations
        fields = ('id','name','description','text','name_kg','description_kg','text_kg',
        'name_en','description_en','text_en','post_date', 'image') 

    def get_photo_url(self, event):
        request = self.context.get('request')
        try:
            image_url = event.image.url
            return request.build_absolute_uri('https://creative.kg' + image_url)
        except:
            return None

class CreativeProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = CreativeProject
        fields = ('id','name','description','text','name_kg','description_kg','text_kg',
        'name_en','description_en','text_en','post_date', 'image') 

    def get_photo_url(self, event):
        request = self.context.get('request')
        try:
            image_url = event.image.url
            return request.build_absolute_uri('https://creative.kg' + image_url)
        except:
            return None