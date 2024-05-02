# -*- coding: utf-8 -*-
# filters.py
import django_filters as filters
from django.db.models import Sum

from visit.models import *


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