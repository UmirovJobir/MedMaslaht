from rest_framework import serializers

from django.db import models
from django.db.models import F, Value
from django.db.models.functions import Concat, Cast

from .models import (
    Clinic,
    Specialization,
    Doctor,
    Availability,
)

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['id', 'name', 'icon']


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id', 'name', 'icon']


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['id', 'day', 'start', 'end']


class DoctorSerializer(serializers.ModelSerializer):
    clinic = ClinicSerializer(many=True)
    availabilities = AvailabilitySerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'full_name', 'phone', 'experience', 'specialization', 'image', 'clinic', 'availabilities']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        availabilities = instance.availabilities.values('day').annotate(
            start_end_times=Concat(
                Cast(F('start'), output_field=models.CharField()),
                Value('-'),
                Cast(F('end'), output_field=models.CharField())
            )
        ).values('day', 'start_end_times')

        result = {}
        for availability in availabilities:
            day = availability['day']
            start_end_times = availability['start_end_times'].split('-')
            start, end = start_end_times[0], start_end_times[1]

            if day not in result:
                result[day] = []

            result[day].append({
                'start': start,
                'end': end,
            })

        representation['availabilities'] = result
        return representation
