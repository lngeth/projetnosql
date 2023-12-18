from django.db import models

class Dog(models.Model):
    url = models.CharField(max_length=255)