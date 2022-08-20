from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import LeaveModel


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveModel
        fields = '__all__'