from rest_framework import viewsets
from app.personas.serializers import PersonasSerializer
from app.personas.models import Personas

# Create your views here.

class PersonasView(viewsets.ModelViewSet):
    serializer_class = PersonasSerializer
    queryset = Personas.objects.all()