from django.urls import path
from . import views

app_name = 'yoga_blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:pk>/', views.blog, name='blog'),
]
