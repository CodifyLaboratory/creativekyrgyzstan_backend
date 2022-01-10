from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status, viewsets
from event.models import Event
from .serializers import EventSerializer
from django.db.models import query
from django.shortcuts import render, get_object_or_404

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer