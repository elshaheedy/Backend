from visit.permissions import VisitPermission, RelatedVisitPermission
from visit.pagination      import *
from visit.serializers     import *
from visit.models          import *
from rest_framework   import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from accounts.models import *
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from visit.filters         import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as rest_filters
from accounts.permissions import *

from safedelete import HARD_DELETE, HARD_DELETE_NOCASCADE

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    pagination_class = CustomPagination

   
    filter_backends = [
        DjangoFilterBackend,
        rest_filters.SearchFilter,
        rest_filters.OrderingFilter,
    ]
    filterset_class =  AttachmentFilter

    permission_classes=[IsAuthenticated,CustomPermission]
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Attachment.objects.all()
        else:
            doctor=Doctor.objects.filter(user=self.request.user).first()
            if doctor:
                return Attachment.objects.filter(visit__doctors__in=[doctor])
            return Attachment.objects.filter(visit__patient__user=self.request.user)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'method', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, enum=['soft', 'hard'],
                description='Specify the delete method (soft or hard). Default is soft.'
            )
        ]
    )
    def destroy(self, request, *args, **kwargs):
        if  request.query_params.get('method')=='hard':
                instance = self.get_object()
                instance.delete(force_policy=HARD_DELETE)
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return super().destroy(request, *args, **kwargs)
    def restore(self, request, *args, **kwargs):
        serializer = RestoreAttachmentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        instance = serializer.validated_data['id']
        instance.undelete()
        return Response(status=status.HTTP_200_OK)


    def get_deleted(self, request, *args, **kwargs):
        paginator = self.pagination_class()
        deleted_attachments = Attachment.deleted_objects.all()
        result_page = paginator.paginate_queryset( deleted_attachments, request)
        serializer = self.get_serializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)








class Statistics(GenericViewSet):
    serializer_class=StatisticsSerializer
    filter_backends = [
        DjangoFilterBackend,

    ]
    filterset_class =  StatisticsFilter

    def get(self, request, *args, **kwargs):
     

        data = {
            'total_visits': Visit.objects.count(),
            'total_patients': Patient.objects.count(),
            'total_doctors': Doctor.objects.count(),
            'total_employees': Employee.objects.count(),
        }

        return Response(data)
