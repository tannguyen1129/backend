from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DisasterZone
from .serializers import DisasterZoneSerializer
from django.shortcuts import get_object_or_404

class DisasterZoneAPI(APIView):
    def get(self, request):
        zones = DisasterZone.objects.all()
        serializer = DisasterZoneSerializer(zones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DisasterZoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            if not pk:
                return Response({"error": "ID không được cung cấp."}, status=status.HTTP_400_BAD_REQUEST)

            # Tìm vùng theo ID
            disaster_zone = get_object_or_404(DisasterZone, pk=pk)

            # Xóa vùng
            disaster_zone.delete()
            return Response({"message": "Xóa thành công."}, status=status.HTTP_204_NO_CONTENT)

        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Log lỗi để debug
            print(f"Error: {e}")
            return Response({"error": "Đã xảy ra lỗi trên server."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)