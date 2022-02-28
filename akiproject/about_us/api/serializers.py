from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from about_us.models import AboutUs, Founders, Reports, Supervisory, Advantages, Purpose, Documents


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = '__all__'


class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = '__all__'


class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'


class SupervisorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisory
        fields = '__all__'


class FoundersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founders
        fields = '__all__'        