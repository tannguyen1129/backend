from django.urls import path
from .views import SubscriptionListCreateView

urlpatterns = [
    path('subscribe/', SubscriptionListCreateView.as_view(), name='subscription_list_create'),
]
