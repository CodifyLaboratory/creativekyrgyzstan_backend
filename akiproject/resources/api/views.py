from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status, viewsets
from resources.models import Recommendation, CreativeProject, FormalRegistrations, HeaderText
from .serializers import RecommendationSerializer, FormalRegistrationsSerializer, CreativeProjectSerializer, HeaderTextSerializer
from django.db.models import query
from django.shortcuts import render, get_object_or_404

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

class FormalRegistrationsViewSet(viewsets.ModelViewSet):
    queryset = FormalRegistrations.objects.all()
    serializer_class = FormalRegistrationsSerializer

class CreativeProjectViewSet(viewsets.ModelViewSet):
    queryset = CreativeProject.objects.all()
    serializer_class = CreativeProjectSerializer

class HeaderTextViewSet(viewsets.ModelViewSet):
    queryset = HeaderText.objects.all()
    serializer_class = HeaderTextSerializer