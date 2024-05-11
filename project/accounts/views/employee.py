"""
Views module for the accounts app.

This module contains the views for handling user authentication and account management.
"""


from accounts.services import *
from accounts.models import *
from accounts.serializers import *

from rest_framework import viewsets
from accounts.permissions import  * 



class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Employee model.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [OwnPermission]
    def create(self , request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee=serializer.save()
        
        user=User.objects.create_user(username=serializer.data['national_id'],password=serializer.data['national_id'])
        employee.user=user
        employee.save()
        
        return Response(EmployeeSerializer(employee).data, status=status.HTTP_201_CREATED)


    


