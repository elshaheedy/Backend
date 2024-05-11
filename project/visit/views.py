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
from accounts.permissions import *
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

    permission_classes=[CustomPermission]
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Attachment.objects.all()
        else:
            return Attachment.objects.filter(user=self.request.user)



class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    pagination_class=CustomPagination
    filter_backends = [
        DjangoFilterBackend,
        rest_filters.SearchFilter,
        rest_filters.OrderingFilter,
    ]
    filterset_class =  VisitFilter
    permission_classes=[CustomPermission]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Visit.objects.all()
        else:
            return Visit.objects.filter(user=self.request.user)
    


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
