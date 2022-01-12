from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status, viewsets
from association_member.models import RulesAndPolitics, Members
from .serializers import RulesAndPoliticsSerializer, MembersSerializer
from django.db.models import query
from django.shortcuts import render, get_object_or_404

class RulesAndPoliticsViewSet(viewsets.ModelViewSet):
    queryset = RulesAndPolitics.objects.all()
    serializer_class = RulesAndPoliticsSerializer

class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer