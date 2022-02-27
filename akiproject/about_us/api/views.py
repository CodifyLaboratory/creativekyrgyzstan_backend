from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status, viewsets
from about_us.models import AboutUs, Founders, Reports, Supervisory
from .serializers import AboutUsSerializer, ReportsSerializer, SupervisorySerializer, FoundersSerializer
from django.db.models import query
from django.shortcuts import render, get_object_or_404

class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer


class SupervisoryViewSet(viewsets.ModelViewSet):
    queryset = Supervisory.objects.all()
    serializer_class = SupervisorySerializer  



class FoundersViewSet(viewsets.ModelViewSet):
    queryset = Founders.objects.all()
    serializer_class = FoundersSerializer        