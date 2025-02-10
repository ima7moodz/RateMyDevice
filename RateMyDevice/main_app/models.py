from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    rate = models.DecimalField(max_digits=5,decimal_places=0)
    warrenty_expration_Date =models.DateField()
    opinion = models.TextField(max_length=250)
    likes =models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Reviews(models.Model):
    comments =models.TextField(max_length=250)
    devices = models.ForeignKey(Device, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
