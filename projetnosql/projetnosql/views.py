from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book, Dog
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
    # Retrieve breeds from API
    breeds = []
    if (len(breeds) == 0):
        response = requests.get('https://api.thecatapi.com/v1/breeds?limit=100&api_key=' + os.getenv('DOGAPI_KEY'))
        if response.status_code == 200:
            breeds = response.json()
    
    if request.method == 'POST':
        breed_id = request.POST.get('breed_id')
        response = requests.get('https://api.thedogapi.com/v1/images/search?limit=10&breeds_ids=' + str(breed_id) + '&api_key=' + os.getenv('DOGAPI_KEY'))
        if response.status_code == 200:
            dogs_list = response.json()
            return render(request, 'dogs_search.html', {'breeds': breeds, 'dogs_list': dogs_list})
        return redirect('dogs_search')
    
    return render(request, 'dogs_search.html', {'breeds': breeds})

def add_dog(request):
    url_to_save = request.GET.get('url')
    
    newDog = Dog()
    newDog.url = str(url_to_save)
    newDog.save(using='default')
    newDog.save(using='mongodb')
    
    return redirect('dogs_list')

def dogs_list(request):
    dogsPSQL = Dog.objects.using('default')
    dogsMongo = Dog.objects.using('mongodb')
    return render(request, 'dogs_list.html', {'dogsPSQL': dogsPSQL, 'dogsMongo': dogsMongo})