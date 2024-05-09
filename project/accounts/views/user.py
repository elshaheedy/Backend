
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from accounts.serializers import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView   
from django.http import Http404
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

 
from rest_framework.viewsets import GenericViewSet 
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer




class UserDetails(GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]



class CustomTokenObtainPairView(TokenObtainPairView):
    """
    A custom view for obtaining token pairs (access and refresh tokens) with additional functionality.

    This class extends the TokenObtainPairView provided by the Django REST Framework, allowing customization
    to include user data in the response along with the token pairs.

    Usage:
        This class can be used as a view in Django REST Framework to handle token authentication. It inherits
        functionality from TokenObtainPairView and adds the ability to include user data in the response.

    
    """
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to obtain token pairs. Additionally, it includes user data in the response
        if available.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: An HTTP response containing token pairs along with user data if available.
        """
        response= super().post(request, *args, **kwargs)
        try:
            response.data['user']= UserSerializer(User.objects.get(username=request.data['username'])).data
        except:
            pass

        return response

class CheckNationalIdView(GenericAPIView):
    serializer_class =CheckNationalSerializer
    permission_classes=[AllowAny]
    def post(self,request,*args,**kwargs):
        national_id=request.data['national_id']
        patient=Patient.objects.filter(national_id=national_id).exists()
        doctor=Doctor.objects.filter(national_id=national_id).exists()
        employee=Employee.objects.filter(national_id=national_id).exists()
        if patient or doctor or employee:
            return Response({'exists':True} ,status=status.HTTP_200_OK)
        return Response({'exists':False} ,status=status.HTTP_200_OK)

class CheckEmailView(GenericAPIView):
    """
    A view to check if an email exists in the database.

    This class provides a POST method to check if a given email already exists in the User model.

    Usage:
        This class can be used as a view in Django REST Framework to handle checking if an email exists
        in the database.

    """
    serializer_class =CheckEmailSerializer
    permission_classes=[AllowAny]
    def post(self,request,*args,**kwargs):
        """
        Handles POST requests to check if an email exists in the database.

        Args:
            request (HttpRequest): The HTTP request object containing the email to check.

        Returns:
            Response: An HTTP response indicating whether the email exists or not.
        """
        email=request.data['email']
        patient=Patient.objects.filter(email=email).exists()
        doctor=Doctor.objects.filter(email=email).exists()
        employee=Employee.objects.filter(email=email).exists()
        if patient or doctor or employee:
            return Response({'exists':True} ,status=status.HTTP_200_OK)
        return Response({'exists':False} ,status=status.HTTP_200_OK)

