from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import Patient
from accounts.serializers import *
from accounts.services import *
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import  *
from django.db.models import Prefetch
from django_filters import rest_framework as filters
from accounts.filters         import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as rest_filters

from visit.models.models import Visit



class PatientViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage Patient model.
    """
    queryset = Patient.objects.all()

    serializer_class = PatientSerializer
    
    filter_backends = [
        DjangoFilterBackend,
        rest_filters.SearchFilter,
        rest_filters.OrderingFilter,
    ]
    filterset_class =  PatientFilter

    permission_classes = [CustomPermission]
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Patient.objects.all()
        else:
            doctor=Doctor.objects.filter(user=self.request.user).first()
            if doctor:
                patients=Visit.objects.filter(doctors__in=[doctor]).values('patient').distinct()
                return Patient.objects.filter(id__in=patients)
            
            return Patient.objects.filter(user=self.request.user)
        
    def create(self , request, *args, **kwargs):

        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient=serializer.save()

        user=User.objects.create_user(username=serializer.data['national_id'],password=serializer.data['national_id'])
        patient.user=user
        patient.save()
        
        
        return Response(PatientSerializer(patient).data, status=status.HTTP_201_CREATED)
 