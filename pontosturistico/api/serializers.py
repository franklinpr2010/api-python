from rest_framework.serializers import ModelSerializer
from pontosturistico.models import PontoTuristico
from pontosturistico.models import PontoTuristico


# Serializers define the API representation.
class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ['nome', 'descricao']