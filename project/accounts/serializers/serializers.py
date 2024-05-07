from rest_framework import serializers

from accounts.models import *


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        # fields = '__all__'
        exclude = ['is_deleted']
class PhoneSerializer(serializers.Serializer):
    mobile=serializers.CharField()
class AddressSerializer(serializers.Serializer):

    # street = serializers.CharField(required=False)
    # city = serializers.CharField(required=False)
    # governorate = serializers.CharField(required=False)
    street = serializers.CharField()
    city = serializers.CharField()
    governorate = serializers.CharField()
    class Meta:
        fields = ['governorate', 'city', 'street']


class PatientSerializer(serializers.ModelSerializer):

    image = UserImageSerializer(many=True, read_only=True, source='user.images')
    address =AddressSerializer( required=False)
    phone=PhoneSerializer(PhoneSerializer)
    class Meta:
        model = Patient

    
        exclude = ['is_deleted']
    def validate_address(self, value):
        address_serializer = AddressSerializer(data=value)
        if not address_serializer.is_valid() or value!=address_serializer.data:
            raise serializers.ValidationError("Invalid address")
        return value

     
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = '__all__'
        exclude = ['is_deleted']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        # fields = '__all__'
        exclude = ['is_deleted']



