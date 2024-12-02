from django.db import models
from userauths.models import User

class Notification(models.Model):
    agency = models.CharField(max_length=255, default='', blank=True, null=True)
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)