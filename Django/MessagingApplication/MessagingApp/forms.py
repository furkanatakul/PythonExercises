from django import forms 
from django.forms import ModelForm
from MessagingApp.models import Message

class AddMessageForm(forms.Form):
    nicknameInput = forms.CharField(label="Nickname", max_length=50)
    messageInput = forms.CharField(label="Message", widget=forms.Textarea(attrs={"class":"messageForm"}))

class AddMessageModelForm(ModelForm):
    class Meta:
        model = Message
        fields = ["nickName", "message"]