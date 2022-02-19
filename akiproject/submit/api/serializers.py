from rest_framework import serializers
from submit.models import Submit

class SubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submit
        fields = '__all__'