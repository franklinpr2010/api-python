from rest_framework.viewsets import ModelViewSet
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco


# ViewSets define the view behavior.
class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    #serializer é como quer mostrar, quais os campos, você quer que inclua o json
    serializer_class = EnderecoSerializer