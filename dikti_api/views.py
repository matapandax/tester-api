from multiprocessing import context
from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    url = "https://api.kemdikbud.go.id:8243/pddikti/1.2/pt"
    headers = {
        'Authorization': 'Bearer c2b1f1d8-2669-39a7-8ad0-2004103e317d'
    }
    response = requests.get(url, headers=headers)
    ''' get atribute json'''
    data = response.json()
    context = {
        'data': data
    }
    return render(request, 'home.html', context)

#create view API point 


