from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=100)  # Tên vật tư/vật lực
    quantity = models.PositiveIntegerField()  # Số lượng tồn kho
    unit = models.CharField(max_length=50)  # Đơn vị
    province_or_city = models.CharField(max_length=255, default="Province")
    location = models.CharField(max_length=255)  # Nơi lưu trữ
    updated_at = models.DateTimeField(auto_now=True)  # Thời gian cập nhật

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"

class Personnel(models.Model):
    personnel_name = models.CharField(max_length=100)  # Tên nhân lực
    role = models.CharField(max_length=100)  # Vai trò
    quantity = models.PositiveIntegerField(default="1") 
    availability_status = models.BooleanField(default=True)  # Có sẵn
    location = models.CharField(max_length=255)  # Vị trí
    contact = models.CharField(max_length=50)  # Số liên lạc

    def __str__(self):
        return f"{self.name} - {self.role}"


class DispatchRequest(models.Model):
    requester_name = models.CharField(max_length=100)  # Người yêu cầu
    description = models.TextField()  # Mô tả yêu cầu
    resource_type = models.ForeignKey(Resource, on_delete=models.CASCADE)  # Loại vật tư
    quantity_needed = models.PositiveIntegerField()  # Số lượng cần
    unit = models.CharField(max_length=50, default="units")  # Đơn vị (ví dụ: kg, cái, hộp)
    status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Đang xử lý'), ('Dispatched', 'Đã điều phối'), ('Completed', 'Hoàn thành')],
        default='Pending'
    )

    approval_status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Đang xử lý'), ('Not approved', 'Không phê duyệt'), ('Approved', 'Đã phê duyệt')],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Thời gian tạo

    def __str__(self):
        return f"{self.requester_name} - {self.quantity_needed} {self.unit} - {self.resource_type}"


from django.db import models

class Assignment(models.Model):
    request = models.ForeignKey('DispatchRequest', on_delete=models.CASCADE)
    assigned_resources = models.ManyToManyField(
        'Resource',
        through='ResourceAssignment',
        related_name='assignments',
        verbose_name="Assigned Resources"
    )
    assigned_personnel = models.ManyToManyField(
        'Personnel',
        through='PersonnelAssignment',
        related_name='assignments',
        verbose_name="Assigned Personnel"
    )
    status = models.CharField(
        max_length=50,
        choices=[('In Progress', 'Đang tiến hành'), ('Completed', 'Hoàn thành')],
        default='In Progress'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Phân công cho nhiệm vụ: {self.request.requester_name}"


class ResourceAssignment(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE)
    quantity_assigned = models.PositiveIntegerField()  # Số lượng phân phối
    unit = models.CharField(max_length=50, default="units")  # Đơn vị

    def __str__(self):
        return f"{self.resource.name} - {self.quantity_assigned} {self.unit}"


class PersonnelAssignment(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    personnel = models.ForeignKey('Personnel', on_delete=models.CASCADE)
    role_in_assignment = models.CharField(max_length=100)  # Vai trò trong phân công
    quantity_assigned = models.PositiveIntegerField(default=1)  # Số lượng nhân sự

    def __str__(self):
        return f"{self.personnel.name} - {self.role_in_assignment}"
