from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.TextField()

    def __str__(self) -> str:
        return f"Username: {self.username}, Message: {self.message}"