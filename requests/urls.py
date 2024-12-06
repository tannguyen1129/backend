# urls.py
from django.urls import path
from .views import SupportRequestView

urlpatterns = [
    path('support-requests/', SupportRequestView.as_view(), name='support-request'),
]
