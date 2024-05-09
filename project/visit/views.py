from visit.permissions import VisitPermission, RelatedVisitPermission
from .pagination      import *
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

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    pagination_class = CustomPagination
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
    pagination_class=CustomPagination
    permission_classes=[VisitPermission]
    filter_backends = [
        DjangoFilterBackend,
        rest_filters.SearchFilter,
        rest_filters.OrderingFilter,
    ]
    filterset_class =  VisitFilter
    


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
