# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SupportRequest
from .serializers import SupportRequestSerializer

class SupportRequestView(APIView):
    def post(self, request):
        serializer = SupportRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Yêu cầu hỗ trợ đã được gửi thành công!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        support_requests = SupportRequest.objects.all()
        serializer = SupportRequestSerializer(support_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)