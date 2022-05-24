from rest_framework import serializers
from event.models import Event, EventImages

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventPastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'        


class EventFutureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'                

class EventImagesSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = EventImages
    #     fields = '__all__'

    image = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = EventImages
        fields = ('id','event', 'image')

    def get_photo_url(self, event):
        request = self.context.get('request')
        try:
            image_url = event.image.url
            return request.build_absolute_uri('https://creative.kg' + image_url)
        except:
            return None