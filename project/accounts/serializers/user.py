from rest_framework import serializers
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from accounts.models import *

class PhoneSerializer(serializers.Serializer):
    mobile=serializers.CharField(required=False)

    
class AddressSerializer(serializers.Serializer):

    street = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    governorate = serializers.CharField(required=False)
    class Meta:
        fields = ['governorate', 'city', 'street']
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['password']

class CheckNationalSerializer(serializers.Serializer):
    national_id =serializers.CharField(max_length=255)
class CheckEmailSerializer(serializers.Serializer):
    email =serializers.CharField(max_length=255)




class ChangePasswordSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    new_password = serializers.CharField()

    def validate_user_id(self, value):
        try:
            user = User.objects.get(id=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        return user

    def save(self, **kwargs):
   
        user = self.validated_data['user_id']
        user.set_password(self.validated_data['new_password'])
        user.save()


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = '__all__'

