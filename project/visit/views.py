from visit.permissions import VisitPermission, RelatedVisitPermission
from .pagination      import VisitPagination
from .serializers     import *
from .models          import *
from rest_framework   import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from accounts.models import *
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .filters         import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as rest_filters
class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    pagination_class = VisitPagination
    permission_classes=[RelatedVisitPermission]
    filter_backends = [
        DjangoFilterBackend,
        rest_filters.SearchFilter,
        rest_filters.OrderingFilter,
    ]
    filterset_class =  MeasurementFilter
class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    pagination_class = VisitPagination
    permission_classes=[RelatedVisitPermission]
    filter_backends = [
        DjangoFilterBackend,
        rest_filters.SearchFilter,
        rest_filters.OrderingFilter,
    ]
    filterset_class =  AttachmentFilter
   



class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    pagination_class=VisitPagination
    permission_classes=[VisitPermission]
    filter_backends = [
        DjangoFilterBackend,
        rest_filters.SearchFilter,
        rest_filters.OrderingFilter,
    ]
    filterset_class =  VisitFilter
    def create(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data.pop('visit'))
        serializer.is_valid(raise_exception=True)
        serializer.save()
      
        if request.data.get('measurement'):
            measurement=request.data.pop('measurement')
            measurement['visit']=serializer.data['id']
            measurement=MeasurementSerializer(data=measurement)
            measurement.is_valid(raise_exception=True)
            measurement.save()
     
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
    
class Statistics(GenericViewSet):
    # permission_classes=[IsAuthenticated]
    serializer_class=StatisticsSerializer
    def get (self, request, *args, **kwargs):
        data={
            'total_visits':Visit.objects.count(),
            'total_patients':Patient.objects.count(),
            'total_doctors':Doctor.objects.count(),
            'total_employees':Employee.objects.count(),
        }

        return Response(data)