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

**Aplicando o serviço de token.**

Em Settings

```
 INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',

```

Em urls.py no projeto

```
    urlpatterns = [
        path('', include(router.urls)),
        path('admin/', admin.site.urls),
        path(r'^api-token-auth/', obtain_auth_token),
    ] + static(settings.MEDIA_URL, document_root=settings.STATIC_URL)

```

Após isso digitar a URL no postman:

```
 127.0.0.1:8000/api-token-auth/
 username: ***********
 password: ***********
```

Acesse as outras Urls pelo postman

```
 127.0.0.1:8000/pontoturistico

```

Coloque o token gerado acima no header:
Authorization: Token 8024973d38c65f79ba7301aa97b8e71b17673072








