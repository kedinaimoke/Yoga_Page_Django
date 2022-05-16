from django.shortcuts import render
from .models import Class
from .models import Instructor


# Create your views here.

def classes(request):
    classroom = Class.objects.all()
    return render(request, 'yoga_classes/classes.html', {'classroom': classroom})


def instructors(request):
    tutor = Instructor.objects.all()
    return render(request, 'yoga_classes/instructors.html', {'tutor': tutor})
