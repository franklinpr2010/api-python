# api-python
**Projeto usando Django Rest Framework**  

**Instalar o Django.**  
pip install django  


**Criando um projeto.**  
django-admin startproject pontosturisticos .  

**Criando uma aplicação.**  
django-admin startapp core

**Criando as migrations.**  
python manage.py makemigrations  
python manage.py migrate  

**Criando o super user.**  
python manage.py createsuperuser

**Instalando o rest framework.**   
pip install djangorestframework

**Criando a App Atrações.**
python manage.py startapp atracoes

**Criando o Model de Atraçao.**

```
class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()

    def __str__(self):
        return self.nome

```

**Registrando no Admin.**
```
from django.contrib import admin
from .models import Atracao

admin.site.register(Atracao)
```

**Criando as migrations.**  
python manage.py makemigrations  
python manage.py migrate  

**Criar o diretório api com os arquivos serializers e viewsets.** 

**ViewSets.** 

```
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.models import Atracao

# ViewSets define the view behavior.
class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    #serializer é como quer mostrar, quais os campos, você quer que inclua o json
    serializer_class = AtracoesSerializer
```

**Serializers.**

```
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.models import Atracao

# Serializers define the API representation.
class AtracoesSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ['nome', 'descricao', 'horario_func', 'idade_minima']
        
        
from rest_framework.viewsets import ModelViewSet
from atracoes.api.serializers import AtracoesSerializer
from atracoes.models import Atracao
```

**Quando implementa o ModelViewSet já existe todos os métodos.**

```
class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
```


**Implementando Imagens no projeto.**  

pip install Pillow

Em Settings.py  
#Pasta de imagens  
MEDIA_ROOT = 'imagens'  
MEDIA_URL = '/media/'  


**Implementando os Filters.**  

pip install django-filter  

Em settings:  

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}  

No ViewSet de Atrações colocar:

#campos que quer que filtre
filterset_fields = ['nome', 'descricao']


**Implementando os SearchFilter.**  

````
#queryset = PontoTuristico.objects.all()
#serializer é como quer mostrar, quais os campos, você quer que inclua o json
serializer_class = PontoTuristicoSerializer
filter_backends = (SearchFilter,)
search_fields = ('nome', 'descricao')

````

http://localhost:8000/pontoturistico/?search=teste2


    
    









