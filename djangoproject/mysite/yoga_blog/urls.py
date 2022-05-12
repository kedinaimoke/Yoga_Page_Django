from django.urls import path
from . import views

app_name = 'yoga_blog'

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('singlepost/<int:pk>/', views.singlepost, name='singlepost'),
]
