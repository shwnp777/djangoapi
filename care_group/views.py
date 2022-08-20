from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import CareModel
from .serializers import CareSerializer

# Create your views here.


class CareViewSet(viewsets.ModelViewSet):
    queryset = CareModel.objects.all()
    serializer_class = CareSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
