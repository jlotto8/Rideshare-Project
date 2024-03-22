from django.db import models
from django.conf import settings

# CustomUser model
class CustomUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

# Ride model
class Ride(models.Model):
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rides_as_driver')
    passengers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='rides_as_passenger', blank=True)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    seats_available = models.PositiveIntegerField()

# Schedule model
class Schedule(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    # Add more fields like start time, end time, etc.
