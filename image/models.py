from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')  # Lưu ảnh vào thư mục `media/images/`
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}"
