from django.contrib import admin
from django.contrib.auth.admin import  UserAdmin as BaseUserAdmin
from user.models import User

@admin.register(User)
class userAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username',  'password')}),
        #Nombre del campo, {campos que quiero mostrar}
        ('Informacion Personal', {'fields': ('first_name', 'last_name','email')}),
        ('Otros', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Permisos', {'fields': ('groups', 'user_permissions')}),
        ('Redes Sociales', {'fields': ('web_site', 'twitter')})
    )
