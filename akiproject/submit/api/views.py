from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status, viewsets
from submit.models import Submit
from .serializers import SubmitSerializer
from django.db.models import query
from django.shortcuts import render, get_object_or_404

class SubmitViewSet(viewsets.ModelViewSet):
    queryset = Submit.objects.all()
    serializer_class = SubmitSerializer