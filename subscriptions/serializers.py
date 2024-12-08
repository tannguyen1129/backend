from rest_framework import serializers
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'full_name', 'email', 'phone', 'address', 'created_at']
