from django.contrib import admin
from MessagingApp.models import Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nickname Group',{"fields" : ["nickName"]}),
        ('Message Group',{"fields" : ["message"]})
    ]
    #fields = ["nickName","message"]


admin.site.register(Message,MessageAdmin)