from django.urls import path,include
from rest_framework import routers
from app.areas import views


#versionado de path

router = routers.DefaultRouter()
router.register(r'areas', views.AreasView, 'areas')

urlpatterns = [
    path("", include(router.urls))
]
