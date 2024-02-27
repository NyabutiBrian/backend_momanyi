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
    python --version
    ```

2. **Install Django Project:**

    ```bash
    mkdir backEnd
    cd backEnd

    # Install django with pip in a virtual environment
    sudo apt install python3-pip python3-venv

    # Create virtual environment within the project
    python3 -m venv my_env

    # activate the environment
    source my_env/bin/activate
    # deactivate the environment
    deactivate

    # install django
    pip install django
    pip install djangorestframework
    pip install django-cors-headers
    python -m pip install Pillow
    django-admin startproject allbackend .
    python manage.py collectstatic
    pip freeze > requirements.txt
    python manage.py runserver
    ```

3. **Setup Database, createsuperuser and makemigrations**
    ```bash
    # setup postgresql database
    pip install psycopg2-binary
    pip install python-decouple
    # create createsuperuser
    python manage.py createsuperuser
    # make migrations
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
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