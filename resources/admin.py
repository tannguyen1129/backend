from django.contrib import admin
from .models import Resource, Personnel, DispatchRequest, Assignment, ResourceAssignment, PersonnelAssignment


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'province_or_city', 'location', 'updated_at')
    search_fields = ('name', 'location', 'province_or_city')
    list_filter = ('province_or_city',)
    ordering = ('-updated_at',)


@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('personnel_name', 'role', 'quantity', 'availability_status', 'location', 'contact')
    search_fields = ('personnel_name', 'role', 'location')
    list_filter = ('availability_status', 'role')
    ordering = ('personnel_name',)


@admin.register(DispatchRequest)
class DispatchRequestAdmin(admin.ModelAdmin):
    list_display = ('requester_name', 'resource_type', 'quantity_needed', 'status', 'approval_status', 'created_at')
    search_fields = ('requester_name', 'description', 'resource_type__name')
    list_filter = ('status', 'approval_status', 'created_at')
    ordering = ('-created_at',)


class ResourceAssignmentInline(admin.TabularInline):
    model = ResourceAssignment
    extra = 1


class PersonnelAssignmentInline(admin.TabularInline):
    model = PersonnelAssignment
    extra = 1


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('request', 'status', 'created_at')
    search_fields = ('request__requester_name',)
    list_filter = ('status', 'created_at')
    inlines = [ResourceAssignmentInline, PersonnelAssignmentInline]
    ordering = ('-created_at',)


@admin.register(ResourceAssignment)
class ResourceAssignmentAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'resource', 'quantity_assigned', 'unit')
    search_fields = ('assignment__request__requester_name', 'resource__name')
    list_filter = ('assignment__status',)
    ordering = ('assignment',)


@admin.register(PersonnelAssignment)
class PersonnelAssignmentAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'personnel', 'role_in_assignment', 'quantity_assigned')
    search_fields = ('assignment__request__requester_name', 'personnel__name', 'role_in_assignment')
    list_filter = ('assignment__status',)
    ordering = ('assignment',)
