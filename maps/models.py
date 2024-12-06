from django.db import models

class DisasterZone(models.Model):
    name_zone = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.FloatField()  # Bán kính vùng nguy hiểm
    disaster_type = models.CharField(max_length=50)  # Loại thiên tai
    description = models.TextField()  # Mô tả chi tiết
