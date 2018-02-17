from django.db import models

class TruckModel(models.Model): # Model of the truck model
    name = models.CharField(max_length=50,null=True, blank=True)
    max_weight = models.FloatField()

    def __str__(self):
        return self.name

class Truck(models.Model): # Model of truck
    name = models.CharField(max_length=50,null=True, blank=True)
    model = models.ForeignKey('TruckModel')
    curr_weight = models.FloatField()
    garage_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name
