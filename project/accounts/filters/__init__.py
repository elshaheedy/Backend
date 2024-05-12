# -*- coding: utf-8 -*-
# filters.py
import django_filters as filters
from django.db.models import Sum

from accounts.models import *


class  PatientFilter(filters.FilterSet):
    address__street = filters.CharFilter(lookup_expr='icontains', label='Street')

    class Meta:
        model = Patient
        fields = {
            'user': ['exact'],
            'full_name': ['exact', 'icontains', 'istartswith'],
            'created_at': ['year', 'month', 'day', 'hour', 'minute', 'second', 'gt','lt','gte','lte'],
            'nationality': ['exact', 'icontains', 'istartswith'],
            'national_id': ['exact'],
            'disease_type': ['exact', 'icontains', 'istartswith'],
            'blood_type': ['exact', 'icontains', 'istartswith'],
            # 'address__street': ['exact', 'icontains', 'istartswith'],
            # 'address__city': ['exact', 'icontains', 'istartswith'],
            # 'address__governorate': ['exact', 'icontains', 'istartswith'],
            # 'phone__mobile': ['exact', 'icontains', 'istartswith'],

       

        }

class UserImageFilter(filters.FilterSet):
    class Meta:
        model = UserImage
        fields = {
            'user_id': ['exact'],
            'created_at': ['year', 'month', 'day', 'hour', 'minute', 'second', 'gt','lt','gte','lte'],
        }




class DoctorFilter(filters.FilterSet):
    class Meta:
        model = Doctor
        fields = {
            'user': ['exact'],
            'speciality': ['exact', 'icontains', 'istartswith'],
            'nationality': ['exact', 'icontains', 'istartswith'],
            'national_id': ['exact'],
            'full_name': ['exact', 'icontains', 'istartswith'],
            'created_at': ['year', 'month', 'day', 'hour', 'minute', 'second', 'gt','lt','gte','lte'],
            'experience_years': ['exact'],
            'work_days': ['exact', 'icontains', 'istartswith'],
            'license_number': ['exact', 'icontains', 'istartswith'],
        }

class EmployeeFilter(filters.FilterSet):
    class Meta:
        model = Employee
        fields = {
            'user': ['exact'],
            'national_id': ['exact'],
            'full_name': ['exact', 'icontains', 'istartswith'],
            'created_at': ['year', 'month', 'day', 'hour', 'minute', 'second', 'gt','lt','gte','lte'],
        }