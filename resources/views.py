from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Resource, Personnel, DispatchRequest, Assignment
from .serializers import ResourceSerializer, PersonnelSerializer, DispatchRequestSerializer, AssignmentSerializer
from .permissions import IsAgencyPermission, IsAuthorityPermission
from rest_framework.permissions import IsAuthenticated

class AgencyViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsAgencyPermission]

    def list(self, request):
        """
        Danh sách tài nguyên.
        """
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def personnel(self, request):
        """
        Danh sách nhân lực.
        """
        personnel = Personnel.objects.all()
        serializer = PersonnelSerializer(personnel, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def add_personnel(self, request):
        """
        Thêm nhân lực mới cho agency.
        """
        serializer = PersonnelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Nhân lực mới đã được thêm.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def assignments(self, request):
        """
        Danh sách phân công.
        """
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def dispatch_requests(self, request):
        """
        Danh sách yêu cầu điều phối của agency.
        """
        requests = DispatchRequest.objects.all()
        serializer = DispatchRequestSerializer(requests, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create_dispatch_request(self, request):
        """
        Thêm yêu cầu điều phối tài nguyên.
        """
        serializer = DispatchRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Yêu cầu điều phối đã được tạo.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def create_assignment(self, request):
        """
        Thêm nhân lực và phân công nhân lực và vật tư.
        """
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Phân công đã được tạo.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AuthorityViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsAuthorityPermission]

    def list(self, request):
        """
        Danh sách tài nguyên.
        """
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create_resource(self, request):
        """
        Thêm tài nguyên.
        """
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tài nguyên đã được thêm.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def dispatch_requests(self, request):
        """
        Danh sách yêu cầu điều phối hoặc thông tin chi tiết của một yêu cầu.
        """
        dispatch_id = request.query_params.get('id')  # Lấy tham số `id` từ query parameters

        if dispatch_id:  # Nếu `id` được cung cấp
            try:
                # Tìm yêu cầu điều phối theo `id`
                dispatch_request = DispatchRequest.objects.get(pk=dispatch_id)
            except DispatchRequest.DoesNotExist:
                return Response({'error': 'Yêu cầu không tồn tại.'}, status=status.HTTP_404_NOT_FOUND)

            # Serialize và trả về thông tin chi tiết
            serializer = DispatchRequestSerializer(dispatch_request)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Nếu không có `id`, trả về danh sách toàn bộ
        requests = DispatchRequest.objects.all()
        serializer = DispatchRequestSerializer(requests, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def update_approval_status(self, request):
        """
        Cập nhật trạng thái phê duyệt của yêu cầu điều phối.
        """
        dispatch_id = request.data.get('id')  # Lấy ID từ body của request
        approval_status = request.data.get('approval_status')  # Lấy trạng thái phê duyệt mới

        if not dispatch_id or approval_status is None:
            return Response(
                {'error': 'Cần cung cấp cả id và approval_status.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Lấy yêu cầu điều phối theo ID
            dispatch_request = DispatchRequest.objects.get(pk=dispatch_id)
        except DispatchRequest.DoesNotExist:
            return Response(
                {'error': 'Yêu cầu điều phối không tồn tại.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Cập nhật trạng thái phê duyệt
        dispatch_request.approval_status = approval_status
        dispatch_request.save()

        return Response(
            {'message': 'Trạng thái phê duyệt đã được cập nhật.'},
            status=status.HTTP_200_OK
        )
