from django.db import models
from django.contrib import admin

# Create your models here.
class Personas(models.Model):
    nombres = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)