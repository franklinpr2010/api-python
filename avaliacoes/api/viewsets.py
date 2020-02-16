from rest_framework.viewsets import ModelViewSet
from avaliacoes.api.serializers import AvaliacaoSerializer
from avaliacoes.models import Avaliacao


# ViewSets define the view behavior.
class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    #serializer é como quer mostrar, quais os campos, você quer que inclua o json
    serializer_class = AvaliacaoSerializer