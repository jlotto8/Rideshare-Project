from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Ride, Schedule  # Make sure the import path is correct
from .forms import RideForm
from django.urls import path

from django.http import HttpResponse
from django.views.generic import ListView, DetailView

# Your view functions or class-based views go here

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Render the HTML template named index.html

# def index(request):
#     return HttpResponse("Welcome to the index page!")

@login_required
def profile(request):
    # Render the user's profile page
    user = request.user
    return render(request, 'users/profile.html', {'user': user})

# @login_required
# def create_ride(request):
#     # Create a new ride if the form is valid
#     if request.method == 'POST':
#         form = RideForm(request.POST)
#         if form.is_valid():
#             ride = form.save(commit=False)
#             ride.driver = request.user
#             ride.save()
#             return redirect('ride_created_success')  # Redirect to a success URL or view
#     else:
#         form = RideForm()  # Create a new empty form instance
    
#     # Render the form for creating a ride (with form errors if any)
#     return render(request, 'rides/create_ride.html', {'form': form})


from django.views.generic.edit import CreateView
from .models import Ride
from .forms import RideForm
from django.urls import reverse_lazy

class CreateRideView(CreateView):
    model = Ride
    form_class = RideForm
    template_name = 'ride_create.html'  # Replace 'ride_create.html' with your actual template name
    success_url = reverse_lazy('ride_list')  # Replace 'ride_list' with your actual URL name for the ride list view


@login_required
def join_ride(request, ride_id):
    # Join a ride by adding the current user as a passenger
    ride = get_object_or_404(Ride, id=ride_id)

    if request.user == ride.driver:
        # Prevent the driver from joining their own ride
        return redirect('ride_detail', ride_id=ride.id)  # Redirect to ride detail page or another URL

    if ride.passengers.filter(id=request.user.id).exists():
        # User is already a passenger in this ride
        return redirect('ride_detail', ride_id=ride.id)  # Redirect to ride detail page or another URL

    if ride.seats_available > 0:
        # Add the current user as a passenger and reduce available seats
        ride.passengers.add(request.user)
        ride.seats_available -= 1
        ride.save()
        return redirect('ride_detail', ride_id=ride.id)

