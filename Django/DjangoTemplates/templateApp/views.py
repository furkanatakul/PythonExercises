from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request,"templateApp/first.html")

def weatherView(request):
    weatherDictionary = {"Sariyer" : "30", "Beykoz" : "32", "Fatih": [5,11,12,13], 
                         "Basaksehir" : {"morning" : 10, "evening" : 20},
                         "userPremium" : True, "test" : "test test",
                         }
    return render(request, "templateApp/weather.html",context=weatherDictionary)