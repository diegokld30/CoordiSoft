from django.contrib import admin
from app.personas.models import Personas

# Register your models here.

#admin.site.register(Areas)
@admin.register(Personas)
class AreasAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'correo']