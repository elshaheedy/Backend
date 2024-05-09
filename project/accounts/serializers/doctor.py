from rest_framework import serializers
from accounts.models import Doctor
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        # fields = '__all__'
        exclude = ['is_deleted']
