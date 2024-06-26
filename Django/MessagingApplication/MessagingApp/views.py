from django.shortcuts import render, redirect
from. import models
from django.urls import reverse, reverse_lazy
from MessagingApp.forms import AddMessageForm, AddMessageModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

def listMessage(request):
    allMasseges = models.Message.objects.all()
    messageDictionary = {"messages":allMasseges}
    return render(request,"MessagingApp/listMessage.html",context=messageDictionary)
@login_required(login_url="/login")
def addMessage(request):
    if request.POST:
        message = request.POST["message"] 
        allMasseges = models.Message.objects.create(username=request.user,message=message)
        print(allMasseges.id)
        return redirect(reverse("MessagingApp:listMessage"))
    return render(request,"MessagingApp/addMessage.html")
@login_required(login_url="/login")
def addMessageByForm(request):
    if request.method == "POST":
        form = AddMessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data["messageInput"]
            models.Message.objects.create(username=request.user,message=message)
            return redirect(reverse("MessagingApp:addMessageByForm"))
        else:
            print("Error in form")
            return render(request,"MessagingApp/addMessageByForm.html",context={"form":form})
    else:
        form = AddMessageForm()
        return render(request,"MessagingApp/addMessageByForm.html",context={"form":form})
@login_required(login_url="/login")
def AddMessageByModelForm(request):
    if request.method == "POST":
        form = AddMessageModelForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data["message"]
            models.Message.objects.create(username=request.user,message=message)
            return redirect(reverse("MessagingApp:addMessageByModelForm"))
        else:
            print("Error in form")
            return render(request,"MessagingApp/addMessageByModelForm.html",context={"form":form})
    else:
        form = AddMessageModelForm()
        return render(request,"MessagingApp/addMessageByModelForm.html",context={"form":form})
@login_required
def deleteMessage(request,id1):
    message = models.Message.objects.get(id=id1)
    if request.user == message.username:
        models.Message.objects.get(id=id1).delete()
        return redirect(reverse("MessagingApp:listMessage"))

class SigUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"