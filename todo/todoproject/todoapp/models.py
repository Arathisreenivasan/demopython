from django.db import models

# Create your models here.
from django.db import models

# Create your views here.
class Task(models.Model):
    name=models.CharField(max_length=250)
    priority=models.IntegerField()
    date=models.DateField()


    def __str__(self):
        return self.name