from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import EventViewSet


router = routers.DefaultRouter()
router.register('events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
