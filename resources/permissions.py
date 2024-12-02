from rest_framework.permissions import BasePermission
from userauths.models import User

class IsAgencyPermission(BasePermission):
    """
    Permission chỉ cho phép người dùng có role 'agency' hoặc là admin.
    """
    def has_permission(self, request, view):
        # Admin luôn được phép truy cập
        if request.user and request.user.is_authenticated and request.user.is_staff:
            return True
        
        # Kiểm tra người dùng có role 'agency'
        return (
            request.user and 
            request.user.is_authenticated and 
            request.user.role == 'agency'
        )

class IsAuthorityPermission(BasePermission):
    """
    Permission chỉ cho phép người dùng có role 'authority' hoặc là admin.
    """
    def has_permission(self, request, view):
        # Admin luôn được phép truy cập
        if request.user and request.user.is_authenticated and request.user.is_staff:
            return True
        
        # Kiểm tra người dùng có role 'authority'
        return (
            request.user and 
            request.user.is_authenticated and 
            request.user.role == 'authority'
        )
