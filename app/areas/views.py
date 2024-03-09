from rest_framework import viewsets
from app.areas.serializers import AreasSerializer
from app.areas.models import Areas

# Create your views here.

class AreasView(viewsets.ModelViewSet):
    serializer_class = AreasSerializer
    queryset = Areas.objects.all()