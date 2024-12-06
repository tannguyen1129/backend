from django.urls import path
from .views import CitizenNotificationListView, AgencyNotificationListCreateView, AgencyNotificationDetailView

urlpatterns = [
    path('citizen/notifications/', CitizenNotificationListView.as_view(), name='citizen_notifications'),
    path('agency/notifications/', AgencyNotificationListCreateView.as_view(), name='agency_notifications_list_create'),
    path('agency/notifications/<int:pk>/', AgencyNotificationDetailView.as_view(), name='agency_notification_detail'),
]
