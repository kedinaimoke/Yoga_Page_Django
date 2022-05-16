from django.shortcuts import render, get_object_or_404
from .models import HomeEdit


# Create your views here.

def homepage(request):
    edits = HomeEdit.objects.get()
    return render(request, 'yoga_home/index.html', {})
