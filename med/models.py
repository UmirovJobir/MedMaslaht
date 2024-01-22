from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
                regex=r'^998[0-9]{2}[0-9]{7}$',
                message="Faqat o'zbek raqamlarigina tasdiqlanadi")


class Specialization(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons')

    def __str__(self):
        return self.name


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    experience = models.IntegerField()
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='doctors')

    def __str__(self):
        return self.full_name

