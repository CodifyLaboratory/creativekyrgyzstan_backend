from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status, viewsets
from mainpage.models import MainPage
from .serializers import MainPageSerializer
from django.db.models import query
from django.shortcuts import render, get_object_or_404

class MainPageViewSet(viewsets.ModelViewSet):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer