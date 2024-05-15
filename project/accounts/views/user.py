
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
from accounts.permissions import *
from accounts.filters         import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from accounts.serializers.user import ChangePasswordSerializer
from rest_framework.generics import GenericAPIView,CreateAPIView
from accounts.pagination import CustomPagination
class UserImageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling UserImage model.
    """
    queryset = UserImage.objects.all()
    serializer_class = UserImageSerializer

    filter_backends = [
        DjangoFilterBackend,
        
    ]
    filterset_class =  UserImageFilter
    permission_classes = [IsAuthenticated,CustomPermission]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserImage.objects.all()
        else:
            return UserImage.objects.filter(user=self.request.user)





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
    permission_classes =  [IsAuthenticated,CustomPermission]
    pagination_class = CustomPagination



    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(id=self.request.user.id)



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
        uesr = User.objects.get(username=request.data['username'])
        response.data['user']= UserSerializer(uesr).data
        doctor=Doctor.objects.filter(user=uesr).first()
        if doctor:
            response.data['doctor']= DoctorSerializer(doctor).data
        patient=Patient.objects.filter(user=uesr).first()
        if patient:
            response.data['patient']= PatientSerializer(patient).data
        employee=Employee.objects.filter(user=uesr).first()
        if employee:
            response.data['employee']= EmployeeSerializer(employee).data
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



class ChangePasswordView(GenericAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
       
        if request.user.is_superuser or request.user.is_staff:
            pass 
        else:
            doctor=Doctor.objects.filter(user=request.user).first() 
            if doctor and request.user==serializer.validated_data['user_id']:
                pass
            else:
                return Response({"message": "You are not authorized to change password."}, status=status.HTTP_403_FORBIDDEN)

        serializer.save()
        return Response({"message": "Password changed successfully."}, status=status.HTTP_200_OK)