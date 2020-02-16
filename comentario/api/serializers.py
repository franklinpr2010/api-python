from rest_framework.serializers import ModelSerializer
from comentario.models import Comentario


# Serializers define the API representation.
class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'usuario', 'comentario', 'data', 'aprovado']