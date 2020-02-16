from rest_framework.viewsets import ModelViewSet
from comentario.api.serializers import ComentarioSerializer
from comentario.models import Comentario


# ViewSets define the view behavior.
class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    #serializer é como quer mostrar, quais os campos, você quer que inclua o json
    serializer_class = ComentarioSerializer