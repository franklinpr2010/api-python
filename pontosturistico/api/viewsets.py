from rest_framework.viewsets import ModelViewSet
from pontosturistico.api.serializers import PontoTuristicoSerializer
from pontosturistico.models import PontoTuristico


# ViewSets define the view behavior.
class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    #serializer é como quer mostrar, quais os campos, você quer que inclua o json
    serializer_class = PontoTuristicoSerializer