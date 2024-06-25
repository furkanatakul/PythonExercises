from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    musicianData = models.Musician.objects.all()
    musicianContext = {"Musician" : musicianData}
    return render(request,"databaseApp/index.html", context=musicianContext)