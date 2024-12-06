from django.db import models
from django.utils.timezone import now

class EmergencyNotification(models.Model):
    title = models.CharField(max_length=255)  # Tiêu đề thông báo
    content = models.TextField()  # Nội dung thông báo
    timestamp = models.DateTimeField(default=now)  # Thời gian tạo thông báo

    def __str__(self):
        return self.title

