from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import LeaveModel
from .serializers import LeaveSerializer

# Create your views here.


class LeaveViewSet(viewsets.ModelViewSet):
    queryset = LeaveModel.objects.all()
    serializer_class = LeaveSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
