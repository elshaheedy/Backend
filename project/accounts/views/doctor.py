from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import Doctor
from accounts.serializers import DoctorSerializer
from accounts.services import *
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import  OwnPermission
from django_filters import rest_framework as filters
from accounts.filters         import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as rest_filters


class DoctorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Doctor model.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [OwnPermission]


    
    filter_backends = [
        DjangoFilterBackend,
        rest_filters.SearchFilter,
        rest_filters.OrderingFilter,
    ]
    filterset_class =  PatientFilter


    def create(self , request, *args, **kwargs):
        msg,user=create_user(request.data)
        if msg!="created":
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)

        request.data.update({'user':user.id})
        
        return super().create(request, *args, **kwargs) 
 