from django.shortcuts import render
from rest_framework import generics

from .models import (
    Specialization,
    Doctor,
    Clinic,
    Availability,
    BookedTime,
)
