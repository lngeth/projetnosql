from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Dog
import os
import requests

def index(request):
    return render(request, "index.html");

def dogs_search(request):
    # Retrieve breeds from API
    breeds = []
    if (len(breeds) == 0):
        response = requests.get('https://api.thecatapi.com/v1/breeds?limit=100&api_key=' + os.getenv('DOGAPI_KEY'))
        if response.status_code == 200:
            breeds = response.json()
    
    if request.method == 'POST':
        breed_id = request.POST.get('breed_id')
        breed_name = ""
        for d in breeds:
            if (d['id'] == str(breed_id)):
                breed_name = d['name']
                print(breed_name)
        response = requests.get('https://api.thedogapi.com/v1/images/search?limit=10&breeds_ids=' + str(breed_id) + '&api_key=' + os.getenv('DOGAPI_KEY'))
        if response.status_code == 200:
            dogs_list = response.json()
            return render(request, 'dogs_search.html', {'breeds': breeds, 'dogs_list': dogs_list, 'breed_name_selected': breed_name})
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

def remove_dog_psql(request):
    Dog.objects.using('default').filter(url=str(request.GET.get('url'))).delete()
    return redirect('dogs_list')

def remove_dog_mongo(request):
    Dog.objects.using('mongodb').filter(url=str(request.GET.get('url'))).delete()
    return redirect('dogs_list')