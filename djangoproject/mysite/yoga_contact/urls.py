from django.urls import path
from . import views

app_name = 'yoga_contact'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
]
