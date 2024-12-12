from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)  # Tiêu đề bài viết
    link = models.URLField(unique=True)  # Link đến bài viết, không trùng lặp
    image_url = models.URLField(blank=True, null=True)  # Link hình ảnh (có thể trống)
    time_posted = models.CharField(max_length=100, blank=True, null=True)  # Thời gian đăng bài

    def __str__(self):
        return self.title
