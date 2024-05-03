from rest_framework import serializers
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class UserToGroupSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    group_ids = serializers.ListField(child=serializers.IntegerField())

class PermissionToUserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    permission_ids = serializers.ListField(child=serializers.IntegerField())

class PermissionToGroupSerializer(serializers.Serializer):
    group_id = serializers.IntegerField()
    permission_ids = serializers.ListField(child=serializers.IntegerField())
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['password']

