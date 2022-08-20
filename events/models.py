from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class EventModel(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default='1')
    title = models.CharField(max_length=70)
    body = models.TextField(max_length=1000)
    start_date = models.DateField()
    start_time = models.DateField()
    end_date = models.DateField()
    end_time = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self
