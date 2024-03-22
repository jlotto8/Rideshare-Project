from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Example URL pattern for the index view
    path('about/', views.about, name='about'),  # Example URL pattern for the about view
    # Add more URL patterns as needed for different views or functionalities
]