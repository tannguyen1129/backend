from django.contrib import admin
from .models import DisasterNews

@admin.register(DisasterNews)
class DisasterNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'url')  # Hiển thị các trường trong Admin
    search_fields = ('title', 'description')  # Tìm kiếm theo tiêu đề và mô tả
