# -*- coding: utf-8 -*-
# filters.py
import django_filters as filters
from django.db.models import Sum

from accounts.models import *


class  PatientFilter(filters.FilterSet):
    class Meta:
        model = Patient
        fields = {
            'user': ['exact'],
            'full_name': ['exact'],
            'created_at': ['year', 'month', 'day'],
            'code': ['exact'],
            'nationality': ['exact'],
            'national_id': ['exact'],
            'disease_type': ['exact'],
            'blood_type': ['exact'],
       

        }
class DoctorFilter(filters.FilterSet):
    class Meta:
        model = Doctor
        fields = {
            'user': ['exact'],
            'speciality': ['exact'],
            'nationality': ['exact'],
            'national_id': ['exact'],
            'full_name': ['exact'],
            'created_at': ['year', 'month', 'day'],
            'experience': ['exact'],
            'work_days': ['exact'],
            'license_number': ['exact'],
        }