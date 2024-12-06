from rest_framework import serializers
from .models import DisasterZone

class DisasterZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterZone
        fields = '__all__'
