from rest_framework import serializers
from accounts.models import Doctor
from .user import *
class DoctorSerializer(serializers.ModelSerializer):
    phone=PhoneSerializer(required=False)
    address =AddressSerializer( required=False)
    class Meta:
        model = Doctor
        fields = '__all__'






class RestoreDoctorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    def validate_id(self, value):
        try:
            doctor=Doctor.deleted_objects.get(id=value)
        except Doctor.DoesNotExist:
            raise serializers.ValidationError("Doctor does not exist.")
        return doctor