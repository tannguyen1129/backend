from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    # Hiển thị các trường trong danh sách admin
    list_display = ('question', 'created_at', 'updated_at')
    # Thêm thanh tìm kiếm
    search_fields = ('question', 'answer')
    # Thêm bộ lọc
    list_filter = ('created_at', 'updated_at')
    # Sắp xếp mặc định theo ngày tạo (mới nhất trước)
    ordering = ('-created_at',)
