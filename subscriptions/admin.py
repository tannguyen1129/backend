from django.contrib import admin
from .models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'address', 'created_at')
    search_fields = ('full_name', 'email', 'address')
