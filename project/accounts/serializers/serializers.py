from rest_framework import serializers

from ..models import *


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'
class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        # fields = '__all__'
        exclude = ['is_deleted']
class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        # fields = '__all__'
        exclude = ['is_deleted']
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        # fields = '__all__'
        exclude = ['is_deleted']
class PatientSerializer(serializers.ModelSerializer):
    phone = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        # fields = '__all__'
        exclude = ['is_deleted']
    
    def get_phone(self, obj):
        phones =Phone.objects.filter(user=obj.user)
        return PhoneSerializer(phones, many=True).data
        # return PhoneSerializer(obj.user.phone, many=True).data
    def get_address(self, obj):
        addresses =Address.objects.filter(user=obj.user)
        return AddressSerializer(addresses, many=True).data
    def get_image(self, obj):
        images =UserImage.objects.filter(user=obj.user)
        return UserImageSerializer(images, many=True).data
     
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
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class PositionSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Patient
        fields = '__all__'
    phone = PhoneSerializer(many=True)
    address = AddressSerializer(many=True)
    
class GeneralSerializer(serializers.Serializer):
        postion=PositionSerializer(many=True)
    