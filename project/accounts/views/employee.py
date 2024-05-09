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
   


    


