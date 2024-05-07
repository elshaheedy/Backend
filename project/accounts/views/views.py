"""
Views module for the accounts app.

This module contains the views for handling user authentication and account management.
"""

from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.services import *
# from accounts.swagger_decorators import home_create_schema, home_update_schema
from accounts.models import *
from accounts.serializers import *

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from accounts.permissions import  OwnPermission,  StaffPermission 

class UserImageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling UserImage model.
    """
    queryset = UserImage.objects.all()
    serializer_class = UserImageSerializer
    permission_classes = [OwnPermission]



class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Employee model.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [OwnPermission]
   


    

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response= super().post(request, *args, **kwargs)
        try:
            response.data['user']= UserSerializer(User.objects.get(username=request.data['username'])).data
        except:
            pass

        return response

