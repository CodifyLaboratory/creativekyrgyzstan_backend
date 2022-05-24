from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status, viewsets
from contacts.models import Contact
from .serializers import ContactSerializer
from django.db.models import query
from django.shortcuts import render, get_object_or_404

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer