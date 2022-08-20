from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ProfileViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]