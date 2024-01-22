from django.contrib import admin
from .models import Specialization, Doctor


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'icon']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone', 'experience', 'specialization']
