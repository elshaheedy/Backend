from rest_framework import serializers
from accounts.models import Employee
from .user import *
class EmployeeSerializer(serializers.ModelSerializer):
    phone=PhoneSerializer(required=False)
    address =AddressSerializer( required=False)
    class Meta:
        model = Employee
        # fields = '__all__'
        exclude = ['is_deleted']




class RestoreEmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    def validate_id(self, value):
        try:
            employee=Employee.deleted_objects.get(id=value)
        except Employee.DoesNotExist:
            raise serializers.ValidationError("Employee does not exist.")
        return employee