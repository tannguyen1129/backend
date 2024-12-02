from rest_framework import serializers
from .models import Image

from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'title', 'image', 'image_url', 'uploaded_at']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request and obj.image:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url if obj.image else None