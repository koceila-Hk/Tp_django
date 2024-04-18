from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Govoyage.models import Train
import random

# Create your views here.
def index(request):
    allTrains = list(Train.objects.all())
    return render(request, "Govoyage/accueil.html", {
        "trains" : allTrains,
    })

def show(request, id_train):
    line = Train.objects.get(trainID = id_train)
    return render(request, "Govoyage/detail.html", {
        "trainNb": line.trainID,
        "to" : line.to,
        "time" : line.time,
        "voie" : line.voie,
        "precedent" : int(id_train) - 1,
        "suivant" : int(id_train) + 1,
    })

def random_train(request):
    allTrains = list(Train.objects.all())
    randomLine = random.choice(allTrains)
    return redirect('show', randomLine.trainID)


def search_train(request):
    if request.method == "GET":
        train_id = request.GET.get('train_id')
        if train_id:
            line = get_object_or_404(Train, trainID = train_id)
            return render(request, 'Govoyage/detail.html', {
                'trainNb': line.trainID,
                'to': line.to,
                'time': line.time,
                'voie': line.voie,
                'precedent': int(line.trainID) - 1,
                'suivant': int(line.trainID) + 1,
            })


def add_train(request):
    if request.method == "POST":
        # Récupération des données du formulaire
        train_id = request.POST.get('train_id')
        to = request.POST.get('to')
        time = request.POST.get('time')
        voie = request.POST.get('voie')
        
        # Création d'une nouvelle instance de Train et enregistrement dans la base de données
        new_train = Train.objects.create(trainID=train_id, to=to, time=time, voie=voie)
        new_train.save()
        
        # Redirection vers la page d'accueil
        return redirect('index') 
    else:
        return render(request, 'Govoyage/add_train.html')