from rest_framework import serializers
from event.models import Event, EventImages

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImages
        fields = '__all__'