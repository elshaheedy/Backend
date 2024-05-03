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
router.register('phone', PhoneViewSet)
router.register('address', AddressViewSet)
router.register('user-image', UserImageViewSet)
router.register('group', GroupViewSet)
router.register('permission', PermissionViewSet)
router.register('user-details', UserDetails, basename='user-details')

# from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('postion-create/', PostionCreate.as_view({'post': 'post'}), name='home-create'),
    # path('postion-update/', PostionUpdate.as_view({'post': 'post'}), name='home-update'),
    # path('assign-user-to-groups/', AssignUserToGroups.as_view({'post': 'post'}), name='assign-user-to-groups'),
    # path('assign-permissions-to-user/', AssignPermissionsToUser.as_view({'post': 'post'}), name='assign-permissions-to-user'),
    # path('assign-permissions-to-group/', AssignPermissionsToGroup.as_view({'post': 'post'}), name='assign-permissions-to-group'),
    # path('user-details/<int:user_id>/', UserDetails.as_view({'get': 'retrieve'}), name='user-details'),
    # path('user-details/<int:pk>/', UserDetails.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'}), name='user-details'),

]
