from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return self.username

class Ride(models.Model):
    driver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rides_driven')
    passengers = models.ManyToManyField(CustomUser, related_name='rides_taken')
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination} at {self.departure_time}"

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Schedule(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=10)
    # Add more fields like start time, end time, etc.

    def __str__(self):
        return f"{self.ride.origin} to {self.ride.destination} on {self.day_of_week}"
