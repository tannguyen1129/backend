from django.contrib import admin
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'uploaded_at')  # Các trường hiển thị trong danh sách
    list_filter = ('uploaded_at',)  # Bộ lọc theo ngày tải lên
    search_fields = ('title',)  # Thanh tìm kiếm theo `title`
    ordering = ('-uploaded_at',)  # Sắp xếp giảm dần theo `uploaded_at`
    readonly_fields = ('uploaded_at',)  # Chỉ đọc trường `uploaded_at`

# Đăng ký model Image với ImageAdmin
admin.site.register(Image, ImageAdmin)