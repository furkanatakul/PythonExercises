from django.urls import path
from . import views

#app name register {% app name : view %}  url
app_name="templateApp"

urlpatterns = [
    path("", views.index, name="index"),
    path("weather/", views.weatherView, name="weatherView")
]