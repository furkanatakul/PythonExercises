from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("<int:num1>x<int:num2>/",views.multiplyView,name="multiply"),
    path("<str:item>/",views.programmingLanguages,name="languages"),
    path("<int:num>",views.redirectFunc,name="redirect")
]