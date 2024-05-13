# -*- coding: utf-8 -*-
# filters.py
import django_filters as filters
from django.db.models import Sum

from visit.models import *
from accounts.models import *
from django.db.models import Q


class VisitFilter(filters.FilterSet):


    MEASUREMENT_ATTRIBUTES=['weight','height','blood_pressure','temperature','pulse','oxygen_level']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_address_filters()

    def generate_address_filters(self):
        for attribute in self.MEASUREMENT_ATTRIBUTES:
            field_name = f'measurement__{attribute}'
            lookup_fields = {
                'icontains': 'CharFilter',
                'contains': 'CharFilter',
                'istartswith': 'CharFilter',
                'iexact': 'CharFilter',
                'exact': 'CharFilter',
                'startswith': 'CharFilter',
                # 'gt': 'NumberFilter',
                # 'lt': 'NumberFilter',
                # 'gte': 'NumberFilter',
                # 'lte': 'NumberFilter',
      
            }
               

            for lookup_expr, filter_type in lookup_fields.items():
                filter_name = f'{field_name}__{lookup_expr}'
                filter_class = getattr(filters, filter_type)
                filter_instance = filter_class(field_name=field_name, lookup_expr=lookup_expr)
                self.filters[filter_name] = filter_instance



    class Meta:
        model = Visit
        fields = {
            'ticket': ['exact', 'contains','startswith','iexact','icontains','istartswith'],
            'status': ['exact'],
            'start_at': ['year', 'month', 'day', 'hour', 'minute', 'second', 'gt','lt','gte','lte'],
            'end_at': ['year', 'month', 'day', 'hour', 'minute', 'second', 'gt','lt','gte','lte'],
            'doctors': ['exact'],
            'patient': ['exact'],
            'is_deleted': ['exact'],
            'created_at': ['year', 'month', 'day', 'hour', 'minute', 'second', 'gt','lt','gte','lte'],
            
        }

#         }
class AttachmentFilter(filters.FilterSet):
    class Meta:
        model = Attachment
        fields = {
            'user': ['exact'],
            'visit__patient': ['exact'],
            'visit': ['exact'],
            'kind': ['exact', 'contains','startswith','iexact','icontains','istartswith'],
            'created_at': ['year', 'month', 'day', 'hour', 'minute', 'second', 'gt','lt','gte','lte'],
        }





import django_filters
from django_filters import FilterSet, DateFromToRangeFilter
from django.forms import DateInput
from django_filters import FilterSet, DateFilter

class StatisticsFilter(FilterSet):
    patient_created_at__year = DateFilter(
        field_name='created_at',
        lookup_expr='year',
        label='Created at (Year)'
    )

    patient_created_at__month = DateFilter(
        field_name='created_at',
        lookup_expr='month',
        label='Created at (Month)'
    )

    patient_created_at__day = DateFilter(
        field_name='created_at',
        lookup_expr='day',
        label='Created at (Day)'
    )
    visit_created_at__year = DateFilter(
        field_name='created_at',
        lookup_expr='year',
        label='Created at (Year)'
    )

    visit_created_at__month = DateFilter(
        field_name='created_at',
        lookup_expr='month',
        label='Created at (Month)'
    )

    visit_created_at__day = DateFilter(
        field_name='created_at',
        lookup_expr='day',
        label='Created at (Day)'
    )
# from django_filters import FilterSet, DateFromToRangeFilter, DateFromToRangeFilterWidget

# class StatisticsFilter(django_filters.FilterSet):
#     # patient_created_at__gte = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
#     # patient_created_at__lte = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
#     # visit_created_at__gte  = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
#     # visit_created_at__lte = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
#     created_at = DateFromToRangeFilter(
#         field_name='created_at',
#         widget=DateFromToRangeFilterWidget(attrs={'class': 'datepicker'}),
#         label='Created at (Range)'
#     )