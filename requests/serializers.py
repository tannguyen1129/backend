# serializers.py
from rest_framework import serializers
from .models import SupportRequest

class SupportRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportRequest
        fields = ['full_name', 'id_card', 'phone_number', 'support_type', 'description', 'location']
