from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.models import Atracao


# Serializers define the API representation.
class AtracoesSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ['id', 'nome', 'descricao', 'horario_func', 'idade_minima', 'foto']