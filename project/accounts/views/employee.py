"""
Views module for the accounts app.

This module contains the views for handling user authentication and account management.
"""


from accounts.services import *
from accounts.models import *
from accounts.serializers import *

from rest_framework import viewsets
from accounts.permissions import  * 
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Prefetch
from django_filters import rest_framework as filters
from accounts.filters         import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as rest_filters
from rest_framework.permissions import IsAuthenticated
from accounts.pagination import CustomPagination

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Employee model.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination

    filter_backends = [
        DjangoFilterBackend,
        rest_filters.SearchFilter,
        rest_filters.OrderingFilter,
    ]
    filterset_class =  EmployeeFilter

    permission_classes = [IsAuthenticated,CustomPermission]
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Employee.objects.all()
        else:
               return Employee.objects.filter(user=self.request.user)
         
    def create(self , request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee=serializer.save()
        
        user=User.objects.create_user(username=serializer.data['national_id'],password=serializer.data['national_id'])
        employee.user=user
        employee.save()
        
        return Response(EmployeeSerializer(employee).data, status=status.HTTP_201_CREATED)


    


