"""
Views module for the accounts app.

This module contains the views for handling user authentication and account management.
"""

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.services import *
from accounts.swagger_decorators import home_create_schema, home_update_schema
from .models import *
from .serializers import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from accounts.permissions import  OwnPermission,  StaffPermission 


class PhoneViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Phone model.
    """
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = [OwnPermission]
class AddressViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Address model.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [OwnPermission]

class PatientViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage Patient model.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [OwnPermission]



class DoctorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Doctor model.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [OwnPermission]



class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Employee model.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [OwnPermission]
   


class PostionCreate(GenericViewSet):
    permission_classes = [StaffPermission]
    serializer_class = GeneralSerializer
    # @home_create_schema()
    def post(self, request, *args, **kwargs):

        data= postion_create(request.data)
        return Response(data, status=status.HTTP_201_CREATED)
 
class PostionUpdate(GenericViewSet):
    permission_classes = [StaffPermission]
    serializer_class = GeneralSerializer
    # @home_update_schema()
    def post(self, request, *args, **kwargs):

        data= postion_update(request.data)
        return Response(data, status=status.HTTP_200_OK)
    

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response= super().post(request, *args, **kwargs)
        try:
            response.data['user']= UserSerializer(User.objects.get(username=request.data['username'])).data
        except:
            pass

        return response

