# admin.py
from django.contrib import admin
from .models import SupportRequest

class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'id_card', 'support_type', 'location', 'created_at')
    search_fields = ('full_name', 'phone_number', 'id_card', 'support_type', 'location')
    list_filter = ('support_type', 'created_at')
    readonly_fields = ('created_at',)

admin.site.register(SupportRequest, SupportRequestAdmin)
