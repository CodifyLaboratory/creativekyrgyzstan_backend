from rest_framework import serializers
from association_member.models import RulesAndPolitics, Members

class RulesAndPoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RulesAndPolitics
        fields = '__all__'

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'