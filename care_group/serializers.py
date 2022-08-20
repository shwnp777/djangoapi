from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import CareModel


class CareSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareModel
        fields = '__all__'