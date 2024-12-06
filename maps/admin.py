from django.contrib import admin
from .models import DisasterZone

@admin.register(DisasterZone)
class DisasterZoneAdmin(admin.ModelAdmin):
    # Hiển thị các trường trong danh sách admin
    list_display = ('name_zone', 'latitude', 'longitude', 'radius', 'disaster_type')
    # Thêm thanh tìm kiếm
    search_fields = ('name_zone', 'disaster_type', 'description')
    # Thêm bộ lọc
    list_filter = ('disaster_type',)
    # Các trường có thể chỉnh sửa trực tiếp trong danh sách
    list_editable = ('radius',)
