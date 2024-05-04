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

    phone = PhoneSerializer(many=True, read_only=True, source='user.phones')
    address = AddressSerializer(many=True,read_only=True, source='user.addresses')
    image = UserImageSerializer(many=True, read_only=True, source='user.images')



    class Meta:
        model = Patient
        # fields =['id','disease_type', 'blood_type','user', 'full_name', 'email', 'gender', 'marital_status', 'nationality', 'national_id', 'date_of_birth', 'notes', 'code', 'address', 'phone', 'image']

    
        exclude = ['is_deleted']
    # def to_representation(self, instance):
    # #         # Override to_representation method to prefetch related objects
    #         instance = Patient.objects.select_related('user').prefetch_related('user__phones', 'user__addresses').get(pk=instance.pk)

    #         return super().to_representation(instance)
     
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
    