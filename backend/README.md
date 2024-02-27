## DJANGO + DJANGO REST FRAMEWORK

## Table of contents

- [Overview](#overview)
    - [Introduction](#introduction)
- [Django Content](#django-content)
- [Useful Resources](#useful-resources)
- [Author](#author)

## Overview

### Introduction
- Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

- Django REST framework is a powerful and flexible toolkit for building Web APIs.

## Django + Django REST framework Content

### Create Django Project (Ubuntu)

1. **Install Python:**

    ```bash
    # Check python version
    python3 --version
    ```

2. **Install Django Project:**

    ```bash
    mkdir backend
    cd backend

    # Install django with pip in a virtual environment
    sudo apt install python3-pip python3-venv

    # Create virtual environment within the project
    python3 -m venv .venv

    # activate the environment
    source .venv/bin/activate
    # deactivate the environment
    deactivate

    # install django
    pip install django
    pip install djangorestframework
    pip install django-cors-headers
    pip install Pillow 
    django-admin startproject allbackend .
    # update settings.py

    #env variables
    pip install python-dotenv
    # update settings.py

    python manage.py runserver
    ```

3. **Setup Database, createsuperuser, makemigrations and collectstatics**

    ```bash
    # setup postgresql database
    pip install psycopg2-binary
    pip install python-decouple
    # update settings.py

    # make migrations
    python manage.py makemigrations
    python manage.py migrate
    
    # create createsuperuser
    python manage.py createsuperuser
    pip install -U django-jazzmin # User Interface
    # update settings.py

    # create folder static, collect static files
    python manage.py collectstatic
    # update settings.py
    # update urls.py

    python manage.py runserver
    ```

4. **Create application, api and url endpoint**

    ```python
    # 1. create app
    python manage.py createapp farewell
    # update settings.py

    # 2. create models
    class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    # 3. register models in admin.py
    from .models import ContactMessage
    # CHANGING TABLE LAYOUT
    class ContactMessageAdmin(admin.ModelAdmin):
        list_display = ('id', 'full_name', 'email', 'message', 'message_date')
        list_filter = ['message_date']
    # Register your models here.
    admin.site.register(ContactMessage, ContactMessageAdmin)

    # 4. serialize
    from rest_framework.serializers import ModelSerializer
    from .models import ContactMessage

    class ContactMessageSerializer(ModelSerializer):
        class Meta:
            model = ContactMessage
            fields = ('id', 'full_name', 'email', 'message', 'message_date')

    # 5. create view
    from rest_framework.viewsets import ModelViewSet
    from .models import ContactMessage
    from .serializers import ContactMessageSerializer
    # Create your views here.
    class ContactMessageView(ModelViewSet):
        queryset = ContactMessage.objects.all()
        serializer_class = ContactMessageSerializer

    # 6. create urls
    from django.urls import path
    from rest_framework.routers import DefaultRouter
    from .views import ContactMessageView

    post_router = DefaultRouter()
    post_router.register(r'contactus', ContactMessageView)

    urlpatterns = post_router.urls

    # 7. Update allbackend urls.py
    path('farewell/api/', include('farewell.urls')),
    ```

5. **Host on Render**

    ```python
    pip install gunicorn
    pip install psycopg2-binary

    # collect all requirements
    pip freeze > requirements.txt

    # In render settings
    # add environment variables and
    gunicorn allbackend.wsgi:application
    ```

6. **Update allbackend settings.py**

    ```python
    from pathlib import Path
    from dotenv import load_dotenv
    import os
    load_dotenv()

    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = int(os.environ.get("DEBUG", default=0))
    ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

    INSTALLED_APPS = [
        'jazzmin',
        'corsheaders',
        'rest_framework',
        'farewell.apps.FarewellConfig',
    ]

    CORS_ALLOWED_ORIGINS = ['http://localhost:5173', 'http://192.168.0.17:5173']

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DB'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': os.environ.get('POSTGRES_HOST'),
            'PORT': os.environ.get('POSTGRES_PORT'),
        }
    }

    # Static Files and Media Files
    STATIC_URL = 'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

    #Jazzmin UI
    JAZZMIN_SETTINGS = {
        "site_title": "Momanyi Admin",
        "site_header": "Momanyi Backend",
        "site_brand": "Momanyi Admin",
    }
    ```

7. **Update allbackend urls.py**

    ```python
        from django.contrib import admin
        from django.urls import path, include
        from rest_framework import routers
        from django.conf import settings
        from django.conf.urls.static import static
        from django.contrib.staticfiles.urls import staticfiles_urlpatterns

        router = routers.DefaultRouter()

        urlpatterns = router.urls

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('farewell/api/', include('farewell.urls')),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

        urlpatterns += staticfiles_urlpatterns()
    ```

## Useful Resources
- [Python Official Site](https://www.python.org/)
- [Django Official Site](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django project in Ubuntu](https://www.youtube.com/watch?v=BSRN0hC96L8)
- [Hiding Secret Keys](https://medium.com/@natmakesthings/hiding-secret-key-in-django-deployment-on-heroku-59b9640819a)


**More content to be added, feel free to add any engaging content**

## Author

- Momanyi Brian - [Website](https://momanyi-brian-portfolio.vercel.app)