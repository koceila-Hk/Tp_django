from django.shortcuts import render
from django.http import HttpResponse
from Govoyage.models import Train

# Create your views here.
def index(request):
    allTrains = Train.objects.all()
    return render(request, "Govoyage/accueil.html", {
        "trains" : allTrains,
    })

def show(request, id_train):
    line = Train.objects.get(trainID = id_train)
    return render(request, "Govoyage/detail.html", {
        "to" : line.to,
        "release" : line.time,
        "precedent" : int(id_train) - 1,
        "suivant" : int(id_train) + 1,
    })

def random(request):
    return render(request, "Govoyage/random.html", {
    })
