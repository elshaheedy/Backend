from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import Patient
from accounts.serializers import PatientSerializer
from accounts.services import *
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import  OwnPermission
class PatientViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage Patient model.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [OwnPermission]
    def create(self , request, *args, **kwargs):
        response= postion_create(request.data,PatientSerializer)
        return response
    def update(self, request, *args, **kwargs):
        response= postion_update(self.get_object(),request.data,PatientSerializer)
        return    response

    def partial_update(self, request, *args, **kwargs):
        response= postion_update(self.get_object(),request.data,PatientSerializer)
        return response