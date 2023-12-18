#!/bin/bash 

python manage.py makemigrations projetnosql && python manage.py migrate projetnosql && python manage.py migrate projetnosql --database=mongodb && python manage.py runserver 0.0.0.0:8000