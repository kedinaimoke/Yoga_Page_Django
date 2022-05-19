from django.db import models
from shortuuidfield import ShortUUIDField


# Create your models here.

class Contact(models.Model):
    uuid = ShortUUIDField(unique=True)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return f"{self.email} | {self.uuid}"
