# from django.conf import settings
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from users.models import CustomUser
# from rides.models import Ride
# from .models import CustomUser  
# from .models import Ride
# # from .forms import RideForm

# class CustomUser(AbstractUser):
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     # Add more custom fields as needed

# class Ride(models.Model):
#     driver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rides_as_driver')
#     passengers = models.ManyToManyField(CustomUser, related_name='rides_as_passenger', blank=True)
#     start_location = models.CharField(max_length=255)
#     end_location = models.CharField(max_length=255)
#     departure_time = models.DateTimeField()
#     seats_available = models.PositiveIntegerField()
#     # Add more fields as needed

# class Schedule(models.Model):
#     ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
#     day_of_week = models.CharField(max_length=10)
#     # Add more fields like start time, end time, etc.


from django.db import models
from django.contrib.auth.models import AbstractUser

# Remove these import statements to avoid circular imports
# from users.models import CustomUser
# from rides.models import Ride

# Define your CustomUser model here
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    # Add more custom fields as needed

# Define your Ride model here
class Ride(models.Model):
    driver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rides_as_driver')
    passengers = models.ManyToManyField(CustomUser, related_name='rides_as_passenger', blank=True)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    seats_available = models.PositiveIntegerField()
    # Add more fields as needed

class Schedule(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    # Add more fields like start time, end time, etc.

