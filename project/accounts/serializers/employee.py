from rest_framework import serializers
from accounts.models import Employee
from .user import *
class EmployeeSerializer(serializers.ModelSerializer):
    image = UserImageSerializer( read_only=True, source='user.image')

    phone=PhoneSerializer(required=False)
    address =AddressSerializer( required=False)
    class Meta:
        model = Employee
        fields = '__all__'
    def validate_national_id(self,value):
        user=User.objects.filter(username=value)
        if user:
            raise serializers.ValidationError("national id exits")
        return value



class RestoreEmployeeSerializer(serializers.Serializer):
    id =  serializers.CharField()
    def validate_id(self, value):
        try:
            employee=Employee.deleted_objects.get(id=value)
        except Employee.DoesNotExist:
            raise serializers.ValidationError("Employee does not exist.")
        return employee