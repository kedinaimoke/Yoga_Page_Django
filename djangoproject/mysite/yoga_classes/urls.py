from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'yoga_classes'

urlpatterns = [
    path('classes/', views.classes, name='classes'),
    path('instructors/', views.instructors, name='instructors'),
]

urlpatterns += staticfiles_urlpatterns()
