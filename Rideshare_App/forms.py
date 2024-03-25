from django import forms
from .models import Ride

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['departure_time']

        # fields = ['start_location', 'end_location', 'departure_time', 'seats_available']
        # Optionally, exclude fields or add custom widgets or labels for form fields
