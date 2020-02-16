from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao


# Serializers define the API representation.
class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'usuario', 'nota', 'data']