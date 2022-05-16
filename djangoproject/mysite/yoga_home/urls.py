from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'yoga_home'

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
]

urlpatterns += staticfiles_urlpatterns()
