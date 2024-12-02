from rest_framework import serializers
from .models import Resource, Personnel, DispatchRequest, Assignment, PersonnelAssignment, ResourceAssignment


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = '__all__'


class DispatchRequestSerializer(serializers.ModelSerializer):
    resource_type_details = ResourceSerializer(source='resource_type', read_only=True)

    class Meta:
        model = DispatchRequest
        fields = [
            'id',
            'requester_name',
            'description',
            'resource_type',
            'resource_type_details',  # Thêm thông tin chi tiết về loại tài nguyên
            'quantity_needed',
            'unit',
            'status',
            'approval_status',
            'created_at',
        ]

class ResourceAssignmentSerializer(serializers.ModelSerializer):
    resource_details = ResourceSerializer(source='resource', read_only=True)

    class Meta:
        model = ResourceAssignment
        fields = ['id', 'resource', 'resource_details', 'quantity_assigned', 'unit']

class PersonnelAssignmentSerializer(serializers.ModelSerializer):
    personnel_details = PersonnelSerializer(source='personnel', read_only=True)

    class Meta:
        model = PersonnelAssignment
        fields = ['id', 'personnel', 'personnel_details', 'role_in_assignment', 'quantity_assigned']


class AssignmentSerializer(serializers.ModelSerializer):
    request_details = DispatchRequestSerializer(source='request', read_only=True)
    assigned_resources = ResourceAssignmentSerializer(source='resourceassignment_set', many=True, read_only=True)
    assigned_personnel = PersonnelAssignmentSerializer(source='personnelassignment_set', many=True, read_only=True)

    class Meta:
        model = Assignment
        fields = [
            'id', 'request', 'request_details', 'assigned_resources',
            'assigned_personnel', 'status', 'created_at'
        ]