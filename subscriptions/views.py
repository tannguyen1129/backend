from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription
from .serializers import SubscriptionSerializer

class SubscriptionListCreateView(APIView):
    # GET: Lấy danh sách thông tin đăng ký
    def get(self, request, *args, **kwargs):
        # Lấy toàn bộ danh sách thông tin đăng ký
        queryset = Subscription.objects.all()
        serializer = SubscriptionSerializer(queryset, many=True)
        
        # Trả về dữ liệu với thông điệp
        return Response(
            {"message": "Danh sách đăng ký nhận tin", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    # POST: Đăng ký nhận tin
    def post(self, request, *args, **kwargs):
        # Xác minh và lưu dữ liệu
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Đăng ký nhận thông tin thành công!", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
