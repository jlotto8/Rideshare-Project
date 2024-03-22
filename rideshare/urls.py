"""
URL configuration for rideshare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Rideshare_App import views

urlpatterns = [
    path('', views.index, name='index'),  # URL pattern for the index view
    path('about/', views.about, name='about'),  # URL pattern for the about view
    path('contact/', views.contact, name='contact'),  # URL pattern for the contact view
    # Add more URL patterns as needed for other views or functionalities
]
