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
    


    def create(self , request, *args, **kwargs):
        msg,user=create_user(request.data)
        if msg!="created":
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)

        request.data.update({'user':user.id})
        
        return super().create(request, *args, **kwargs) 
 