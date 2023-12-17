#!/bin/bash 

python manage.py makemigrations projetnosql --no-input && python manage.py migrate --fake projetnosql zero && python manage.py migrate projetnosql --no-input && python manage.py runserver 0.0.0.0:8000