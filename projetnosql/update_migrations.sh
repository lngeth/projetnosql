#!/bin/bash 

python3 ./manage.py makemigrations projetnosql
python3 ./manage.py migrate projetnosql