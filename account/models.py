from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

from .managers import UserManager

phone_regex = RegexValidator(
                regex=r'^998[0-9]{2}[0-9]{7}$',
                message="Faqat o'zbek raqamlarigina tasdiqlanadi")

class User(AbstractUser):    
    username = None
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
