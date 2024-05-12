from rest_framework import serializers
from accounts.models import Doctor
from .user import *
class DoctorSerializer(serializers.ModelSerializer):
    phone=PhoneSerializer(required=False)
    address =AddressSerializer( required=False)
    class Meta:
        model = Doctor
        # fields = '__all__'
        exclude = ['is_deleted']
