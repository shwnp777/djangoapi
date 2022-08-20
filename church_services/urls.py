from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ServiceViewSet

router = routers.DefaultRouter()
router.register('services', ServiceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]