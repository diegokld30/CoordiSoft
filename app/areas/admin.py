from django.contrib import admin
from app.areas.models import Areas

# Register your models here.

#admin.site.register(Areas)
@admin.register(Areas)
class AreasAdmin(admin.ModelAdmin):
    list_display = ['nombre_area', 'created_at']