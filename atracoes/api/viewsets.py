from rest_framework.viewsets import ModelViewSet
from atracoes.api.serializers import AtracoesSerializer
from atracoes.models import Atracao


# ViewSets define the view behavior.
class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    #serializer é como quer mostrar, quais os campos, você quer que inclua o json
    serializer_class = AtracoesSerializer