from rest_framework import serializers

from .models import *


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'
class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
class PatientSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()
    class Meta:
        model = Patient
        fields = '__all__'

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     profile = Profile.objects.create(**profile_data)
    #     patient = Patient.objects.create(profile=profile, **validated_data)
    #     return patient
    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('profile', None)
    #     if profile_data:
    #         profile_serializer = self.fields['profile']
    #         profile_instance = instance.profile
    #         profile_serializer.update(profile_instance, profile_data)
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     return instance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
