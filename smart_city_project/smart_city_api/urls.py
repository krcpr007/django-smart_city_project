from django.urls import path
from .views import ParkingSpaceListCreateView, IrrigationSystemListCreateView

urlpatterns = [
    path('parking/', ParkingSpaceListCreateView.as_view(), name='parking-list-create'),
    path('irrigation/', IrrigationSystemListCreateView.as_view(), name='irrigation-list-create'),
]