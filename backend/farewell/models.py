from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Condolence(models.Model):
    full_name = models.CharField(max_length=100)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
