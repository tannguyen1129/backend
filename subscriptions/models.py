from django.db import models

class Subscription(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Họ và Tên")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Số Điện Thoại")
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name="Khu Vực")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày Đăng Ký")

    def __str__(self):
        return self.email
