from django.db import models

# Create your models here.
class Message(models.Model):
    nickName = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self) -> str:
        return f"Nickname: {self.nickName}, Message: {self.message}"