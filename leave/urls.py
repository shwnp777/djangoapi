from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import LeaveViewSet


router = routers.DefaultRouter()
router.register('leave', LeaveViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

