from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import BookForm, DogsForm
from .models import Book, Categorie
import os
import requests

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            newBook = Book()
            newBook.title = form.cleaned_data.get('title')
            newBook.author = form.cleaned_data.get('author')
            newBook.content = form.cleaned_data.get('content')
            newBook.save(using='default')
            newBook.save(using='mongodb')
            # form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def book_list(request):
    booksPSQL = Book.objects.using('default')
    booksMongo = Book.objects.using('mongodb')
    return render(request, 'book_list.html', {'booksPSQL': booksPSQL, 'booksMongo': booksMongo})

def index(request):
    return HttpResponse("Accueil");

def dogs_search(request):
    if request.method == 'POST':
        form = DogsForm(request.POST)
        if form.is_valid():
            response = requests.get('https://api.thedogapi.com/v1/images/search?limit=10&breed_ids=beng&api_key=' + os.getenv('DOGAPI_KEY'))
            if response.status_code == 200:
                data = response.json()
                print(data)
                return render(request, 'dogs_list.html', {'data': data})
            return redirect('dogs_list')
    else:
        form = DogsForm()
    
    # Retrieve categories from API
    data = []
    categoriesList = Categorie.objects.using('default')
    if (len(categoriesList) == 0):
        response = requests.get('https://api.thecatapi.com/v1/categories?limit=100&api_key=' + os.getenv('DOGAPI_KEY'))
        if response.status_code == 200:
            data = response.json()
            print(data)
    else:
        data = categoriesList
    return render(request, 'dogs_search.html', {'form': form, 'categories': data})

def dogs_list(request):
    return render(request, 'dogs_list.html', {})