from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import EventModel


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventModel
        fields = '__all__'
