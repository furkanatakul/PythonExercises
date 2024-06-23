from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

languageDictionary = {
    "python":"Python Page",
    "c": "C Page",
    "kotlin":"Kotlin Page",
    "java":"Java Page",
    "php":"PHP Page"
    }

def index(request):
    return HttpResponse("This is first Django project index")

def programmingLanguages(request,item):
    try:
        language = languageDictionary[item]
        return HttpResponse(language)
    except:
        return HttpResponseNotFound("Not Found!!, Please look for another language")
        #raise Http404("Not Found!!, Please look for another language")
    # return HttpResponse(languageDictionary.get(item,"Not Found!!"))

def multiplyView(request, num1, num2):
    return HttpResponse(f"{num1} x {num2} = {num1 * num2}")

def redirectFunc(request, num):
    #languageList = list(languageDictionary.keys())
    try:
        language = languageList[num]

        pageToGo = reverse("languages", args=[language])
        return HttpResponseRedirect(pageToGo)
    except:
        return HttpResponseNotFound("Not Found!!, Please look for another language")