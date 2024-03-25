# from django.urls.conf import include  # Import include function

# urlpatterns = [
#     path('', views.index, name='index'),  # URL pattern for the index view
#     path('profile/', views.profile, name='profile'),  # URL pattern for the profile view
#     path('', views.MyListView.as_view(), name='my-list-view'),
#     path('detail/<int:pk>/', views.MyDetailView.as_view(), name='my-detail-view'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('ride/create/', views.CreateRideView.as_view(), name='create_ride.html'),
    path('ride/join/<int:ride_id>/', views.join_ride, name='join_ride'),
]

