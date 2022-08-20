"""ninetynineAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from user_profile.views import MyTokenObtainPairView

urlpatterns = [
    path('api/users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin/', admin.site.urls),
    # path('auth/', obtain_auth_token),
    path('api/', include('user_profile.urls')),
    path('api/', include('leave.urls')),
    path('api/', include('church_services.urls')),
    path('api/', include('posts.urls')),
    path('api/', include('events.urls')),
    path('api/', include('care_group.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configure Admin Titles
admin.site.site_header = "Kaysville Administration"
admin.site.site_title = "Kaysville Administration"
admin.site.index_title = "Welcome to the Kaysville Administration Area"
