# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SupportRequest
from .serializers import SupportRequestSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from resources.permissions import IsAgencyPermission

class SupportRequestView(APIView):
    def get_permissions(self):
        """
        Assign permissions based on the request method.
        - POST: AllowAny (Citizen không cần đăng nhập).
        - GET: IsAuthenticated và IsAgencyPermission (chỉ cho Agency và Admin).
        """
        if self.request.method == 'POST':
            return [AllowAny()]
        elif self.request.method == 'GET':
            return [IsAuthenticated(), IsAgencyPermission()]
        return super().get_permissions()

    def post(self, request):
        serializer = SupportRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Yêu cầu hỗ trợ đã được gửi thành công!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        self.check_permissions(request)  # Ensure permissions are checked for GET

        support_requests = SupportRequest.objects.all()
        serializer = SupportRequestSerializer(support_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)