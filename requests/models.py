# models.py
from django.db import models

class SupportRequest(models.Model):
    full_name = models.CharField(max_length=255)
    id_card = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    support_type = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.support_type}"
