"""
Views module for the accounts app.

This module contains the views for handling user authentication and account management.
"""

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import *
from .serializers import *


class PatientViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Patient model.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# class ProfileViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet for handling Profile model.
#     """
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
class PhoneViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Phone model.
    """
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
class AddressViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Address model.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
class DoctorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Doctor model.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Employee model.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class SignUpView(GenericViewSet):
    """
    ViewSet for handling user signup.
    """
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "message": "User Created Successfully.  Now perform Login to get your token",
            }, status=201)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response= super().post(request, *args, **kwargs)
        try:
            response.data['user']= UserSerializer(User.objects.get(username=request.data['username'])).data
        except:
            pass

        return response
