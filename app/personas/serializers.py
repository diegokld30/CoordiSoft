from rest_framework.serializers import ModelSerializer
from app.areas.models import Areas

class PersonasSerializer(ModelSerializer):
    class Meta:
        model = Areas
        #fields = ['nombre_area','sede', 'created_at']
        fields = '__all__'