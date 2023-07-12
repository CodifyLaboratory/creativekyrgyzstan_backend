from rest_framework import serializers
from submit.models import Submit

class SubmitSerializer(serializers.ModelSerializer):
    company_logo = serializers.SerializerMethodField('get_report_url')

    class Meta:
        model = Submit
        fields = ('id','company_name','full_name','position','company_reg_date','company_members','company_webpage',
        'facebook','telegram','whatsapp','instagram','twitter','tiktok','company_logo',
        'company_field','company_activity','company_email','company_phone') 

    def get_report_url(self, submit):
        request = self.context.get('request')
        try:            
            logo_url = submit.company_logo.url
            return request.build_absolute_uri(logo_url)
        except ValueError:
            return None