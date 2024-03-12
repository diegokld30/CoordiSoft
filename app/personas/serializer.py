from rest_framework.serializers import ModelSerializer
from app.personas.models import Personas

class PersonasSerializer(ModelSerializer):
    class Meta:
        model = Personas
        #fields = ['nombre_area','sede', 'created_at']
        fields = '__all__'