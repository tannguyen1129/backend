from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('role', 'agency_name', 'phone_number', 'address'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('role', 'agency_name', 'phone_number', 'address'),
        }),
    )
    list_display = ('username', 'email', 'role', 'agency_name', 'phone_number')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'role', 'agency_name', 'phone_number')
    ordering = ('username',)

# Register the custom User model
admin.site.register(User, CustomUserAdmin)
