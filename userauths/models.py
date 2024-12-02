from django.db import models
from django.contrib.auth.models import AbstractUser

# Choices for user roles
ROLE_CHOICES = [('agency', 'Cơ quan cứu nạn cứu hộ'), ('citizen', 'Người dân'), ('authority', 'Cơ quan quản lý vật tư')]

# Custom User Model
class User(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    agency_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
