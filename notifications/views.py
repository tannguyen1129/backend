from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EmergencyNotification
from .serializers import EmergencyNotificationSerializer
from resources.permissions import IsAgencyPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Citizen API: Xem danh sách thông báo
class CitizenNotificationListView(APIView):
    """
    API cho công dân xem danh sách thông báo.
    """
    def get(self, request):
        notifications = EmergencyNotification.objects.all().order_by('-timestamp')  # Sắp xếp theo thời gian mới nhất
        serializer = EmergencyNotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Agency API: Tạo thông báo mới
class AgencyNotificationListCreateView(ListCreateAPIView):
    """
    API cho phép Agency tạo hoặc xem danh sách thông báo.
    """
    queryset = EmergencyNotification.objects.all()
    serializer_class = EmergencyNotificationSerializer
    permission_classes = [IsAuthenticated, IsAgencyPermission]

    def perform_create(self, serializer):
        # Có thể thêm logic, ví dụ gán thông tin người tạo (nếu cần)
        serializer.save()


# Agency API: Cập nhật hoặc xóa thông báo
class AgencyNotificationDetailView(RetrieveUpdateDestroyAPIView):
    """
    API cho phép Agency cập nhật hoặc xóa thông báo cụ thể.
    """
    queryset = EmergencyNotification.objects.all()
    serializer_class = EmergencyNotificationSerializer
    permission_classes = [IsAuthenticated, IsAgencyPermission]

