
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from accounts.serializers import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView   

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer



from drf_yasg.utils import swagger_auto_schema
 
from rest_framework.viewsets import GenericViewSet
class AssignUserToGroups(GenericViewSet):
    serializer_class = UserToGroupSerializer
    @swagger_auto_schema(operation_id="assign_user_to_groups")
    def post(self, request):
        # Assuming the request data contains the user id and group ids
        # Example: {'user_id': 1, 'group_ids': [1, 2]}
        data = request.data
        user = User.objects.get(id=data['user_id'])
        groups = Group.objects.filter(id__in=data['group_ids'])
        user.groups.set(groups)
        return Response({'message': 'User assigned to groups successfully'})



class AssignPermissionsToUser(GenericViewSet):
    serializer_class = PermissionToUserSerializer
    @swagger_auto_schema(operation_id="assign_permissions_to_user")
    def post(self, request, user_id):
        # Assuming the request data contains a list of permission ids to assign
        permission_ids = request.data.get('permission_ids', [])
        
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        permissions = Permission.objects.filter(id__in=permission_ids)
        user.user_permissions.set(permissions)
        
        return Response({'message': 'Permissions assigned to user successfully'}, status=status.HTTP_200_OK)
