from rest_framework import serializers
from about_us.models import AboutUs, Reports, Supervisory

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'


class SupervisorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisory
        fields = '__all__'