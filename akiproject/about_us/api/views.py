from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status, viewsets
from about_us.models import AboutUs, Founders, Reports, Supervisory, Advantages, Purpose, Documents, DocumentsPol, AboutPictures
from .serializers import AboutPicturesSerializer, AboutUsSerializer, ReportsSerializer, SupervisorySerializer,\
     FoundersSerializer, AdvantagesSerializer, PurposeSerializer, DocumentsSerializer, DocumentsPolSerializer
from django.db.models import query
from django.shortcuts import render, get_object_or_404


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    
class AboutPicturesViewSet(viewsets.ModelViewSet):
    queryset = AboutPictures.objects.all()
    serializer_class = AboutPicturesSerializer

class PurposeViewSet(viewsets.ModelViewSet):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer


class AdvantagesViewSet(viewsets.ModelViewSet):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer


class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer


class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer


class DocumentsPolViewSet(viewsets.ModelViewSet):
    queryset = DocumentsPol.objects.all()
    serializer_class = DocumentsPolSerializer


class SupervisoryViewSet(viewsets.ModelViewSet):
    queryset = Supervisory.objects.all()
    serializer_class = SupervisorySerializer  


class FoundersViewSet(viewsets.ModelViewSet):
    queryset = Founders.objects.all()
    serializer_class = FoundersSerializer        