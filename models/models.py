from django.db import models

class Airports(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        
# Create your models here.
class Flight(models.Model):
    name = models.CharField(max_length=255)
    destination = models.ForeignKey(Destination, related_name='destination', on_delete=models.DO_NOTHING)
    airports = models.ManyToManyField(Airports)

    def __str__(self):
        return self.name