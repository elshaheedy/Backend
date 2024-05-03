from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import Doctor
from accounts.serializers import DoctorSerializer
from accounts.services import *
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import  OwnPermission


class DoctorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Doctor model.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [OwnPermission]
    def create(self , request, *args, **kwargs):
        response= postion_create(request.data,DoctorSerializer)
        return response
    def update(self, request, *args, **kwargs):
        response= postion_update(self.get_object(),request.data, DoctorSerializer)
        return    response

    def partial_update(self, request, *args, **kwargs):
        response= postion_update(self.get_object(),request.data, DoctorSerializer)
        return response