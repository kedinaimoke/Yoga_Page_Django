from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'yoga_about'

urlpatterns = [
    path('about/', views.about, name='about'),
]

urlpatterns += staticfiles_urlpatterns()
