from rest_framework import serializers
from association_member.models import RulesAndPolitics, Members

class RulesAndPoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RulesAndPolitics
        fields = '__all__'
        depth = 1

class MembersSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = Members
        fields = ('id','submit','photo','bio',) 
        depth = 1

    def get_photo_url(self, report):
        request = self.context.get('request')
        try:
            photo_url = report.photo.url
            return request.build_absolute_uri('https://creative.kg' + photo_url)
        except:
            return None