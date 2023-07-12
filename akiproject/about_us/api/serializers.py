from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from about_us.models import AboutUs, Founders, Reports, Supervisory, Advantages, Purpose, Documents, DocumentsPol,  AboutPictures


class AboutUsSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = AboutUs
        fields = ('id','picture', 'description', 'description_kg', 'description_en') 

    def get_image_url(self, aboutus):
        request = self.context.get('request')
        try:
            image_url = aboutus.picture.url
            return request.build_absolute_uri('https://creative.kg' + image_url)
        except ValueError:
            return None

class AboutPicturesSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = AboutPictures
        fields = ('id','picture') 

    def get_image_url(self, aboutus):
        request = self.context.get('request')
        try:
            image_url = aboutus.picture.url
            return request.build_absolute_uri('https://creative.kg' + image_url)
        except ValueError:
            return None


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = '__all__'


class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = '__all__'


class ReportsSerializer(serializers.ModelSerializer):
    report_text = serializers.SerializerMethodField('get_report_url')

    class Meta:
        model = Reports
        fields = ('id','name','short_description','name_kg','short_description_kg','name_en','short_description_en',
        'report_text','created_date','signature','add_info', 'add_info_kg','add_info_en',) 

    def get_report_url(self, report):
        request = self.context.get('request')
        try:
            report_url = report.report_text.url
            return request.build_absolute_uri('https://creative.kg' + report_url)
        except ValueError:
            return None
            


class DocumentsSerializer(serializers.ModelSerializer):
    rule_doc = serializers.SerializerMethodField('get_rule_url')

    class Meta:
        model = Documents
        fields = ('id','rule_doc','name','name_kg','name_en') 

    def get_rule_url(self, about):
        request = self.context.get('request')
        try:
            rule_url = about.rule_doc.url
            return request.build_absolute_uri('https://creative.kg' + rule_url)
        except ValueError:
            return None

class DocumentsPolSerializer(serializers.ModelSerializer):
    politic_doc = serializers.SerializerMethodField('get_politic_url')

    class Meta:
        model = DocumentsPol
        fields = ('id','politic_doc','name','name_kg','name_en') 

    def get_politic_url(self, about):
        request = self.context.get('request')
        try:
            politic_url = about.politic_doc.url
            return request.build_absolute_uri('https://creative.kg' + politic_url)
        except ValueError:
            return None

class SupervisorySerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = Supervisory
        fields = ('id','member','photo','add_info',)
        depth = 2

    def get_photo_url(self, supervisor):
        request = self.context.get('request')
        try:
            image_url = supervisor.photo.url
            return request.build_absolute_uri('https://creative.kg' + image_url)
        except ValueError:
            return None


class FoundersSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = Founders
        fields = ('id','founder','image','info',)
        depth = 2

    def get_photo_url(self, founder):
        request = self.context.get('request')
        try:
            image_url = founder.image.url
            return request.build_absolute_uri('https://creative.kg' + image_url)
        except ValueError:
            return None    