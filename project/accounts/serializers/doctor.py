from rest_framework import serializers
from accounts.models import Doctor
from .user import *
class DoctorSerializer(serializers.ModelSerializer):
    image = UserImageSerializer( read_only=True, source='user.image')
    phone=PhoneSerializer(required=False)
    address =AddressSerializer( required=False)
    class Meta:
        model = Doctor
        fields = '__all__'


    def validate_national_id(self,value):
        user=User.objects.filter(username=value)
        if user:
            raise serializers.ValidationError("national id exits")
        return value



class RestoreDoctorSerializer(serializers.Serializer):
    id = serializers.CharField()
    def validate_id(self, value):
        try:
            doctor=Doctor.deleted_objects.get(id=value)
        except Doctor.DoesNotExist:
            raise serializers.ValidationError("Doctor does not exist.")
        return doctor