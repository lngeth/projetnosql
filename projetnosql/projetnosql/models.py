from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    
class Categorie(models.Model):
    name = models.CharField(max_length=100)