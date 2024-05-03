
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from accounts.serializers import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView   
from django.http import Http404

 
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer




class UserDetails(GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
