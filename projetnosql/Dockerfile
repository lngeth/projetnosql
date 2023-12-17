FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DOGAPI_KEY live_C1w7Pomv3NL05tqRxE4vkH5DAIC86XtRlURPZaepOOJswFCFW0Cx0DZ1fqyxH19N

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate

# Exécutez la commande pour démarrer le serveur Django
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]



