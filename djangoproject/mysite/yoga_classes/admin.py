from django.contrib import admin
from .models import Class
from .models import Instructor

# Register your models here.

admin.site.register(Class)
admin.site.register(Instructor)
