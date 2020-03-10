from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


# ViewSets define the view behavior.
class PontoTuristicoViewSet(ModelViewSet):
    #queryset = PontoTuristico.objects.all()
    #serializer é como quer mostrar, quais os campos, você quer que inclua o json
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao')
    #Alterando o comportamento padrão com o lookup field
    lookup_field = 'nome'

    '''
        Esse metodo sempre deve ser usado quando o queryset não está definido, sobrescrevendo esse metodo
        só filtre se realmente achar conveniente.
    '''
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.filter(pk=id)
        if id:
            queryset = PontoTuristico.objects.filter(id=id)
        if nome:
            queryset = PontoTuristico.objects.filter(nome__iexact=nome)
        if descricao:
            queryset = PontoTuristico.objects.filter(nome__iexact=descricao)
        return PontoTuristico.objects.filter(aprovado = True)

    '''
        Toda vez que mandar o metodo GET chama esse metodo list, se tirar o list volta a retornar o ponto turistico
        Ele muda o comportamento padrão
        
    def list(self, request, *args, **kwargs):
        return Response({'teste':123})
    '''

    '''
    Ele muda o comportamento padrão, sobrescrevendo o create para dar a resposta que achar conveniente
    Sobrescrevendo o create.
    '''
    def create(self, request, *args, **kwargs):
        #chamando o metodo principal
       return super(PontoTuristicoViewSet, self).create()

    def destroy(self, request, *args, **kwargs):
        # chamando o metodo principal
        return super(PontoTuristicoViewSet, self).destroy()

    def retrieve(self, request, *args, **kwargs):
        # chamando o metodo principal
        return super(PontoTuristicoViewSet, self).retrieve()

    def update(self, request, *args, **kwargs):
        # chamando o metodo principal
        return super(PontoTuristicoViewSet, self).update()

    def partial_update(self, request, *args, **kwargs):
        # chamando o metodo principal
        return super(PontoTuristicoViewSet, self).partial_update()

    '''
    Customizado -o action é um decorator que vai implementar os metodos: GET, POST, DELETE e etc
    Para chamar esse metodo http://localhost:8000/pontoturistico/1/denunciar
     '''
    @action(methods=['get', 'post'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=True)
    def teste(self, request):
        pass
