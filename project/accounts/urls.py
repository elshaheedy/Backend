'''
Module for defining URL patterns for accounts app.
'''
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import *

router = routers.DefaultRouter()
router.register('patient', PatientViewSet)
router.register('employee', EmployeeViewSet)
router.register('doctor', DoctorViewSet)
# router.register('profile', ProfileViewSet)
router.register('phone', PhoneViewSet)
router.register('address', AddressViewSet)

# from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('signup/', SignUpView.as_view({'post':'create'}), name='signup'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('patient/', PatientViewSet.as_view({'get': 'list'}), name='patient_list'),
    # path('employee/', EmployeeViewSet.as_view({'get': 'list'}), name='employee_list'),
    # path('doctor/', DoctorViewSet.as_view({'get': 'list'}), name='doctor_list'),
    # path('profile/', ProfileViewSet.as_view({'get': 'list'}), name='profile_list'),
    # path('phone/', PhoneViewSet.as_view({'get': 'list'}), name='phone_list'),
    # path('address/', AddressViewSet.as_view({'get': 'list'}), name='address_list'),

    # path('patient/<int:pk>/', PatientViewSet.as_view({'get': 'retrieve'}), name='patient_detail'),
    # path('employee/<int:pk>/', EmployeeViewSet.as_view({'get': 'retrieve'}), name='employee_detail'),
    # path('doctor/<int:pk>/', DoctorViewSet.as_view({'get': 'retrieve'}), name='doctor_detail'),
    # path('profile/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve'}), name='profile_detail'),
    # path('phone/<int:pk>/', PhoneViewSet.as_view({'get': 'retrieve'}), name='phone_detail'),
    # path('address/<int:pk>/', AddressViewSet.as_view({'get': 'retrieve'}), name='address_detail'),

    # # path('signup/', UserViewSet.as_view({'post': 'create'}), name='signup'),

    # path('profile/<int:pk>/', ProfileViewSet.as_view({'delete': 'destroy'}), name='profile_delete'),
    # path('phone/<int:pk>/', PhoneViewSet.as_view({'delete': 'destroy'}), name='phone_delete'),
    # path('address/<int:pk>/', AddressViewSet.as_view({'delete': 'destroy'}), name='address_delete'),
    # path('patient/<int:pk>/', PatientViewSet.as_view({'delete': 'destroy'}), name='patient_delete'),
    # path('employee/<int:pk>/', EmployeeViewSet.as_view({'delete': 'destroy'}), name='employee_delete'),
    # path('doctor/<int:pk>/', DoctorViewSet.as_view({'delete': 'destroy'}), name='doctor_delete'),

    # path('patient/', PatientViewSet.as_view({'post': 'create'}), name='patient_create'),
    # path('employee/', EmployeeViewSet.as_view({'post': 'create'}), name='employee_create'),
    # path('doctor/', DoctorViewSet.as_view({'post': 'create'}), name='doctor_create'),
    # path('profile/', ProfileViewSet.as_view({'post': 'create'}), name='profile_create'),
    # path('phone/', PhoneViewSet.as_view({'post': 'create'}), name='phone_create'),
    # path('address/', AddressViewSet.as_view({'post': 'create'}), name='address_create'),

    # path('profile/<int:pk>/', ProfileViewSet.as_view({'put': 'update'}), name='profile_update'),
    # path('phone/<int:pk>/', PhoneViewSet.as_view({'put': 'update'}), name='phone_update'),
    # path('address/<int:pk>/', AddressViewSet.as_view({'put': 'update'}), name='address_update'),
    # path('patient/<int:pk>/', PatientViewSet.as_view({'put': 'update'}), name='patient_update'),
    # path('employee/<int:pk>/', EmployeeViewSet.as_view({'put': 'update'}), name='employee_update'),
    # path('doctor/<int:pk>/', DoctorViewSet.as_view({'put': 'update'}), name='doctor_update'),

    # path('profile/<int:pk>/', ProfileViewSet.as_view({'patch': 'partial_update'}), name='profile_partial_update'),
    # path('phone/<int:pk>/', PhoneViewSet.as_view({'patch': 'partial_update'}), name='phone_partial_update'),
    # path('address/<int:pk>/', AddressViewSet.as_view({'patch': 'partial_update'}), name='address_partial_update'),
    # path('patient/<int:pk>/', PatientViewSet.as_view({'patch': 'partial_update'}), name='patient_partial_update'),
    # path('employee/<int:pk>/', EmployeeViewSet.as_view({'patch': 'partial_update'}), name='employee_partial_update'),
    # path('doctor/<int:pk>/', DoctorViewSet.as_view({'patch': 'partial_update'}), name='doctor_partial_update'),


]
