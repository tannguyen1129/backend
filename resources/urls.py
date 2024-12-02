from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgencyViewSet, AuthorityViewSet

# Khởi tạo router
router = DefaultRouter()

# Đăng ký ViewSet
router.register(r'agency', AgencyViewSet, basename='agency')
router.register(r'authority', AuthorityViewSet, basename='authority')

# Cấu hình urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Đưa các endpoint từ router vào URL chính
]
