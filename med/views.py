from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import F, Value
from django.db.models.functions import Concat, Cast
from django.db import models

from rest_framework import generics, views, response

from .models import (
    Specialization,
    Doctor,
    Clinic,
    Availability,
    BookedTime,
)

from .serializers import (
    SpecializationSerializer,
    DoctorSerializer,
    AvailabilitySerializer
)


class SpecializationView(generics.ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class DoctorView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['specialization']



class AvailabilityView(views.APIView):
    def get(self, request, *args, **kwargs):
        availabilities = Availability.objects.filter(doctor_id=self.kwargs['pk']).annotate(
            start_end_times=Concat(
                Cast(F('start'), output_field=models.CharField()),
                Value('-'),
                Cast(F('end'), output_field=models.CharField())
            )
        ).values(
            'day', 'start_end_times'
        )

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
        
        return response.Response({'availabilities': result})