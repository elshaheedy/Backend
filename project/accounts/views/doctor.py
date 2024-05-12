from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import Doctor
from accounts.serializers import DoctorSerializer
from accounts.services import *
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import  *
from django_filters import rest_framework as filters
from accounts.filters         import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as rest_filters

from accounts.pagination import CustomPagination

class DoctorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Doctor model.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = CustomPagination

    
    filter_backends = [
        DjangoFilterBackend,
        rest_filters.SearchFilter,
        rest_filters.OrderingFilter,
    ]
    filterset_class =  DoctorFilter

    permission_classes = [IsAuthenticated,CustomPermission]
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Doctor.objects.all()
        else:
            return Doctor.objects.filter(user=self.request.user)
    

    def create(self , request, *args, **kwargs):
        serializer = DoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doctor=serializer.save()
        
        user=User.objects.create_user(username=serializer.data['national_id'],password=serializer.data['national_id'])
        doctor.user=user
        doctor.save()
        
        return Response(DoctorSerializer(doctor).data, status=status.HTTP_201_CREATED)
 