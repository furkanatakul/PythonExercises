from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request,"templateApp/first.html")

def weatherView(request):
    weatherDictionary = {"Sarıyer" : "30", "Beykoz" : "32", "Fatih": [10,11,12,13], "Başakşehir" : {"morning" : 10, "evening" : 20}}
    return render(request, "templateApp/weather.html",context=weatherDictionary)