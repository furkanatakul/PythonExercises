from django.shortcuts import render, redirect
from. import models
from django.urls import reverse
from MessagingApp.forms import AddMessageForm, AddMessageModelForm
# Create your views here.
def listMessage(request):
    allMasseges = models.Message.objects.all()
    messageDictionary = {"messages":allMasseges}
    return render(request,"MessagingApp/listMessage.html",context=messageDictionary)
def addMessage(request):
    if request.POST:
        nickname = request.POST["nickname"]
        message = request.POST["message"] 
        models.Message.objects.create(nickName=nickname,message=message)
        return redirect(reverse("MessagingApp:listMessage"))
    return render(request,"MessagingApp/addMessage.html")
def addMessageByForm(request):
    if request.method == "POST":
        form = AddMessageForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nicknameInput"]
            message = form.cleaned_data["messageInput"]
            models.Message.objects.create(nickName=nickname,message=message)
            return redirect(reverse("MessagingApp:addMessageByForm"))
        else:
            print("Error in form")
            return render(request,"MessagingApp/addMessageByForm.html",context={"form":form})
    else:
        form = AddMessageForm()
        return render(request,"MessagingApp/addMessageByForm.html",context={"form":form})
def AddMessageByModelForm(request):
    if request.method == "POST":
        form = AddMessageModelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickName"]
            message = form.cleaned_data["message"]
            models.Message.objects.create(nickName=nickname,message=message)
            return redirect(reverse("MessagingApp:addMessageByModelForm"))
        else:
            print("Error in form")
            return render(request,"MessagingApp/addMessageByModelForm.html",context={"form":form})
    else:
        form = AddMessageModelForm()
        return render(request,"MessagingApp/addMessageByModelForm.html",context={"form":form})