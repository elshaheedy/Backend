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

