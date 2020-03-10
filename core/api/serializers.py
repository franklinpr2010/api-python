from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from core.models import PontoTuristico


# Serializers define the API representation.
class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado']