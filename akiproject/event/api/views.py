from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status
from event.models import Event
from .serializers import EventSerializer, CreateEventSerializer
from django.db.models import query
from django.shortcuts import render, get_object_or_404

class EventViewSet(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request, pk=None):  # get
        event_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(event_object)
        return Response(serializer.data)