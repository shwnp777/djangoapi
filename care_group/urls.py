from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import CareViewSet


router = routers.DefaultRouter()
router.register('care', CareViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
