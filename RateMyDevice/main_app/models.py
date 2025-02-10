



from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    rate = models.DecimalField(max_digits=5,decimal_places=2)
    warrenty_expration_Date =models.DateField()
    opinion = models.TextField(max_length=250)
    likes =models.IntegerField(default=0)

    def __str__(self):
        return self.name