from django.db import models
from django.contrib import admin

from app.areas.models import Areas


# Create your models here.
class Personas(models.Model):
    nombres = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    FK_area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    #FK_ficha = models.ForeignKey(Fichas, on_delete=models.CASCADE)


    created_at = models.DateTimeField(auto_now_add=True)