# -*- coding: utf-8 -*-
# filters.py
import django_filters as filters
from django.db.models import Sum

from accounts.models import *
from .user import *
    



class PatientFilter(filters.FilterSet):
    ADDRESS_ATTRIBUTES=['street','city','country']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_address_filters()

    def generate_address_filters(self):
        for attribute in self.ADDRESS_ATTRIBUTES:
            field_name = f'address__{attribute}'
            lookup_fields = {
                # 'contains': 'CharFilter',
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
        model = Patient
        fields = {
            'user': ['exact'],
            'full_name': ['exact', 'icontains', 'istartswith','contains','startswith','iexact'],
            'created_at': ['year', 'month', 'day', 'hour', 'minute', 'second', 'gt','lt','gte','lte'],
            'nationality': ['exact', 'icontains', 'istartswith','contains','startswith','iexact'],
            'national_id': ['exact'],
            'disease_type': ['exact', 'contains', 'startswith', 'iexact', 'icontains', 'istartswith'],
            'blood_type': ['exact', 'contains', 'startswith', 'iexact', 'icontains', 'istartswith'],


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