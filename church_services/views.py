from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import ServiceModel
from .serializers import ServiceSerializer

# Create your views here.


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer
    # permission_classes = (IsAuthenticated,)