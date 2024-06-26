from django import forms 
from django.forms import ModelForm
from MessagingApp.models import Message

class AddMessageForm(forms.Form):
    messageInput = forms.CharField(label="Message", widget=forms.Textarea(attrs={"class":"messageForm"}))

class AddMessageModelForm(ModelForm):
    class Meta:
        model = Message
        fields = ["message"]