from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import Patient
from accounts.serializers import PatientSerializer
from accounts.services import *
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import  OwnPermission
from django.db.models import Prefetch
class PatientViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage Patient model.
    """
    queryset = Patient.objects.all()

    serializer_class = PatientSerializer
    permission_classes = [OwnPermission]
    def get_queryset(self):
            queryset = Patient.objects.select_related('user').prefetch_related('user__phones', 'user__addresses', 'user__images').all()
            return queryset
    

    def create(self , request, *args, **kwargs):
        response= postion_create(request.data,PatientSerializer)
        return response
    def update(self, request, *args, **kwargs):
        response= postion_update(self.get_object(),request.data,PatientSerializer)
        return    response

    def partial_update(self, request, *args, **kwargs):
        response= postion_update(self.get_object(),request.data,PatientSerializer)
        # return    response
        if response.status_code == status.HTTP_200_OK:
            return Response(PatientSerializer(self.get_object()).data, status=status.HTTP_200_OK)
        else:
            return Response(response.data, status=status.HTTP_400_BAD_REQUEST)