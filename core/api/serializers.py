from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from core.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer


# Serializers define the API representation.
class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    descricao_completa = SerializerMethodField()
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto' , 'atracoes', 'comentarios', 'avaliacoes', 'endereco',
                  'descricao_completa', 'get_descricao_completa2']

    def get_descricao_completa(self, obj):
        return 's% - %s' %(obj.nome, obj.descricao)