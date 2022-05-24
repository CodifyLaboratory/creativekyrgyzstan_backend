from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status, viewsets
from submit.models import Submit
from .serializers import SubmitSerializer
from django.db.models import query
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

@permission_classes([AllowAny])
class SubmitViewSet(viewsets.ModelViewSet):
    queryset = Submit.objects.all()
    serializer_class = SubmitSerializer