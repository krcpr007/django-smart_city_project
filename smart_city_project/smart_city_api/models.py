from django.db import models

class ParkingSpace(models.Model):
    location = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

class IrrigationSystem(models.Model):
    area = models.CharField(max_length=255)
    moisture_level = models.IntegerField(default=0)
