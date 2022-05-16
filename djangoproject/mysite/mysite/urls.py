"""mysite URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('yoga_blog/', include('yoga_blog.urls', namespace='yoga_blog')),
    path('yoga_home/', include('yoga_home.urls', namespace='yoga_home')),
    path('yoga_contact/', include('yoga_contact.urls', namespace='yoga_contact')),
    path('yoga_classes/', include('yoga_classes.urls', namespace='yoga_classes')),
    path('yoga_about/', include('yoga_about.urls', namespace='ypga_About')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
