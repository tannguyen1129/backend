from rest_framework import serializers
from .models import EmergencyNotification

class EmergencyNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyNotification
        fields = ['id', 'title', 'content', 'timestamp']
