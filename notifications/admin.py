from django.contrib import admin
from .models import EmergencyNotification

@admin.register(EmergencyNotification)
class EmergencyNotificationAdmin(admin.ModelAdmin):
    # Cấu hình hiển thị danh sách trong admin
    list_display = ('id', 'title', 'timestamp')  
    list_filter = ('timestamp',)  
    search_fields = ('title', 'content')  
    ordering = ('-timestamp',) 
    date_hierarchy = 'timestamp'  
