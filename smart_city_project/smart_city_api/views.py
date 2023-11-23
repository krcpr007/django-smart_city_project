from rest_framework import generics
from .models import ParkingSpace, IrrigationSystem
from .serializers import ParkingSpaceSerializer, IrrigationSystemSerializer

class ParkingSpaceListCreateView(generics.ListCreateAPIView):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer

class IrrigationSystemListCreateView(generics.ListCreateAPIView):
    queryset = IrrigationSystem.objects.all()
    serializer_class = IrrigationSystemSerializer