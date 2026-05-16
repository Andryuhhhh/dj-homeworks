from rest_framework import serializers
from .models import Sensor, Measurement

class MeasurementSerializer(serializers.ModelSerializer):
    measurement_time = serializers.DateTimeField(source='created_at', read_only=True)

    class Meta:
        model = Measurement
        fields = ['temperature', 'measurement_time']

class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']