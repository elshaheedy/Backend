from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import Patient
from accounts.serializers import *
from accounts.services import *
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import  OwnPermission
from django.db.models import Prefetch
from django_filters import rest_framework as filters
from accounts.filters         import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as rest_filters

class UserImageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling UserImage model.
    """
    queryset = UserImage.objects.all()
    serializer_class = UserImageSerializer
    permission_classes = [OwnPermission]


class PatientViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage Patient model.
    """
    queryset = Patient.objects.all()

    serializer_class = PatientSerializer
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
 