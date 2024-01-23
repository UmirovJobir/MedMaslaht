from django.db import models
from account.models import phone_regex, User


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/clinics')

    def __str__(self):
        return self.name

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/specializations')

    def __str__(self):
        return self.name


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    experience = models.IntegerField()
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='doctors')
    image = models.ImageField(upload_to='doctors')
    clinic = models.ManyToManyField(Clinic, related_name='clinics')

    def __str__(self):
        return self.full_name


class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availabilities')
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])


class BookedTime(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='booked_times')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.DateField()