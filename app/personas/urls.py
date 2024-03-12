from django.urls import path,include
from rest_framework import routers
from app.personas import views


#versionado de path

router = routers.DefaultRouter()
router.register(r'', views.PersonasView, 'areas')

urlpatterns = [
    path("", include(router.urls))
]
