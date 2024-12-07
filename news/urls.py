from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DisasterNewsViewSet

router = DefaultRouter()
router.register(r'news', DisasterNewsViewSet, basename='news')

urlpatterns = [
    # Các URL khác
    path('weather/', include(router.urls)),  # Định nghĩa endpoint API
]
