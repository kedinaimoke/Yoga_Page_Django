from django.db import models


# Create your models here.

class Class(models.Model):
    class_name = models.CharField(max_length=200)
    class_about = models.TextField()
    class_date = models.DateField()
    class_time = models.TimeField()

    def __str__(self):
        return f"{self.class_name}"


class Instructor(models.Model):
    instructor_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.instructor_name}"
