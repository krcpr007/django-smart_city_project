# smart_city_api/serializers.py

from rest_framework import serializers
from .models import ParkingSpace, IrrigationSystem

class ParkingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpace
        fields = '__all__'

class IrrigationSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrrigationSystem
        fields = '__all__'
