from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    salary = models.IntegerField(null=True)
    def __str__(self) -> str:
        return f"Name: {self.name}, Instrument: {self.instrument}, Age: {self.age}, Salary: {self.salary}"