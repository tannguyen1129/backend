from django.db import models

class DisasterNews(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    image_url = models.URLField(blank=True, null=True)
    published_at = models.DateTimeField()
