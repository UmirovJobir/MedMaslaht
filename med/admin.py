from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Specialization,
    Doctor,
    Clinic,
    Availability,
    BookedTime,
)


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'clinic_icon']
    readonly_fields = ['clinic_icon']

    def clinic_icon(self, obj):
        return format_html('<img src="%s" width="50px"/>'%(obj.icon.url))

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'special_icon']
    readonly_fields = ['special_icon']

    def special_icon(self, obj):
        return format_html('<img src="%s" width="50px"/>'%(obj.icon.url))


class AvailabilityInline(admin.TabularInline):
    model = Availability
    extra = 0

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    inlines = [AvailabilityInline]
    list_display = ['id', 'full_name', 'phone', 'experience', 'specialization']


@admin.register(BookedTime)
class BookedTimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor', 'user', 'start_time', 'end_time', 'day']
