from . import views
from django.urls import path

app_name = "MessagingApp"

urlpatterns = [
    path('', views.listMessage, name="listMessage"),
    path('addMessage/', views.addMessage, name="addMessage"),
    path('addMessageByForm/', views.addMessageByForm, name="addMessageByForm"),
    path('addMessageByModelForm/', views.AddMessageByModelForm, name="addMessageByModelForm"),
    path('signup/', views.SigUpView.as_view(), name="signup"),
    path('deleteMessage/<int:id1>', views.deleteMessage, name="deleteMessage")
]
