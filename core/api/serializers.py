from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from atracoes.models import Atracao
from core.models import PontoTuristico, DocIdentificacao
from core.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer
from enderecos.models import Endereco


class DocIndetificacaoSerializer(ModelSerializer):
    class Meta:
        model: DocIdentificacao
        #mostra todos os filtros
        fields = '__all__'


# Serializers define the API representation.
class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    descricao_completa = SerializerMethodField()
    doc_identificacao = DocIndetificacaoSerializer()
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto' , 'atracoes', 'comentarios', 'avaliacoes', 'endereco',
                  'descricao_completa', 'get_descricao_completa2', 'doc_identificacao']

    def get_descricao_completa(self, obj):
        return'%s - %s' %  {obj.nome} - {obj.descricao}


    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.all(at)

    '''
    
    '''
    def create(self, validated_data):
        #atracao
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        #doc_identificacao
        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)
        ponto.doc_identificacao = doc

        #endereco
        endereco = validated_data['endereco']
        del validated_data['endereco']
        end = Endereco.objects.create(**endereco)
        ponto.endereco = end

        ponto.save()
        return ponto


