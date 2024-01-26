from django.urls import path

from .views import (
    SpecializationView,
    DoctorView,
    AvailabilityView
)


urlpatterns = [
    path('special/', SpecializationView.as_view(), name='special'),
    path('doctor/', DoctorView.as_view(), name='doctor'),
    # path('doctor/<int:pk>/', AvailabilityView.as_view(), name='doctor'),
]