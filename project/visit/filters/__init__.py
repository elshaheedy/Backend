# -*- coding: utf-8 -*-
# filters.py
import django_filters as filters
from django.db.models import Sum

from visit.models import *
from accounts.models import *

class VisitFilter(filters.FilterSet):
    class Meta:
        model = Visit
        fields = {
            'ticket': ['exact'],
            'datatime': ['year', 'month', 'day'],
            'doctors': ['exact'],
            'patient': ['exact'],
            'is_deleted': ['exact'],
            'created_at': ['year', 'month', 'day']
            
        }
class MeasurementFilter(filters.FilterSet):
    class Meta:
        model = Measurement
        fields = {
            'visit': ['exact'],
            'height': ['exact'],
            'weight': ['exact'],
            'blood_pressure': ['exact'],
            'temperature': ['exact'],
            'pulse': ['exact'],
            'oxygen_level': ['exact'],
            'created_at': ['year', 'month', 'day']
        }
class AttachmentFilter(filters.FilterSet):
    class Meta:
        model = Attachment
        fields = {
            'visit': ['exact'],
            'kind': ['exact'],
            'created_at': ['year', 'month', 'day']
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