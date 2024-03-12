from rest_framework import viewsets
from app.areas.serializers import AreasSerializer
from app.personas.models import Personas

# Create your views here.

class PersonasView(viewsets.ModelViewSet):
    serializer_class = AreasSerializer
    queryset = Personas.objects.all()