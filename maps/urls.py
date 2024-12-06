from django.urls import path
from .views import DisasterZoneAPI

urlpatterns = [
    path('disaster-zones/', DisasterZoneAPI.as_view(), name='disaster-zones'),
    path('disaster-zones/<int:pk>/', DisasterZoneAPI.as_view(), name='disaster-zone-detail'),
]
