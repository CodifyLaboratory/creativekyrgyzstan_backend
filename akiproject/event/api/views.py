from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status, viewsets, permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action, permission_classes
from event.models import Event, EventImages
from .serializers import EventSerializer, EventImagesSerializer, EventPastSerializer, EventFutureSerializer
from django.db.models import query
from django.shortcuts import render, get_object_or_404
from datetime import date
from django.contrib.sites.shortcuts import get_current_site

# @permission_classes([IsAuthenticatedOrReadOnly])
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventPastViewSet(viewsets.ModelViewSet):
    today = date.today()
    queryset = Event.objects.filter(event_date__lt=today)
    serializer_class = EventPastSerializer
   

class EventFutureViewSet(viewsets.ModelViewSet):
    today = date.today()
    queryset = Event.objects.filter(event_date__gte=today)
    serializer_class = EventFutureSerializer

class EventImagesViewSet(viewsets.ModelViewSet):
    queryset = EventImages.objects.all()
    serializer_class = EventImagesSerializer
    

    # def get(self, request, *args, **kwargs):
    #     queryset = EventImages.objects.all()
    #     serializer = EventImagesSerializer(queryset, many=True, context={"request":request})
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    