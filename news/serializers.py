from rest_framework import serializers
from .models import DisasterNews

class DisasterNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterNews
        # Các trường bạn muốn trả về qua API
        fields = ['id', 'title', 'description', 'url', 'image_url', 'published_at']

