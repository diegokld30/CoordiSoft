from django.db import models
from django.contrib import admin

# Create your models here.
class Areas(models.Model):
    nombre_area = models.CharField(max_length=255)
    sede = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)