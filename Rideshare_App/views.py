from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Ride, Schedule
from .forms import RideForm
from django.urls import path


@login_required
def profile(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})

@login_required
def create_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            # Create a new Ride instance with form data
            ride = form.save(commit=False)
            
            # Assign the current user (driver) to the ride
            ride.driver = request.user
            
            # Save the ride to the database
            ride.save()
            
            # Optionally, add success message or redirect to a success page
            return redirect('ride_created_success')  # Redirect to a success URL or view
    else:
        form = RideForm()  # Create a new empty form instance
    
    # Render the form for creating a ride (with form errors if any)
    return render(request, 'rides/create_ride.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect
from .models import Ride

def join_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)

    if request.user == ride.driver:
        # Prevent the driver from joining their own ride
        # You can add a message or redirect to a different page
        return redirect('ride_detail', ride_id=ride.id)  # Redirect to ride detail page or another URL

    if ride.passengers.filter(id=request.user.id).exists():
        # User is already a passenger in this ride
        # You can add a message or redirect to a different page
        return redirect('ride_detail', ride_id=ride.id)  # Redirect to ride detail page or another URL

    if ride.seats_available > 0:
        # Add the current user as a passenger and reduce available seats
        ride.passengers.add(request.user)
        ride.seats_available -= 1
        ride.save()

        # Optionally, add a success message or redirect to a success page
        return redirect('ride_detail', ride_id=ride.id)  # Redirect to ride detail page or another URL
    else:
        # Ride is already full, handle accordingly
        # You can add a message or redirect to a different page
        return redirect('ride_detail', ride_id=ride.id)  # Redirect to ride detail page or another URL


def view_schedule(request):
    # Retrieve schedules based on user's criteria (e.g., day of week, location, etc.)
    schedules = Schedule.objects.filter(day_of_week='Monday')
    return render(request, 'schedules/view_schedule.html', {'schedules': schedules})