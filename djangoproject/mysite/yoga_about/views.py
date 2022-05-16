from django.shortcuts import render
from .models import Update


# Create your views here.

def about(request):
    updates = Update.objects.all()
    return render(request, 'yoga_about/about.html', {'updates': updates})
