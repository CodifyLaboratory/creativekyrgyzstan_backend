from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status, viewsets, permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action, permission_classes
from event.models import Event, EventImages
from .serializers import EventSerializer, EventImagesSerializer
from django.db.models import query
from django.shortcuts import render, get_object_or_404

# @permission_classes([IsAuthenticatedOrReadOnly])
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventImagesViewSet(viewsets.ModelViewSet):
    queryset = EventImages.objects.all()
    serializer_class = EventImagesSerializer