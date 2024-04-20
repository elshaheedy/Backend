# -*- coding: utf-8 -*-
# permissions.py
from rest_framework.permissions import  BasePermission


class RelatedVisitPermission(BasePermission):
   
    
    def has_permission(self, request, view):
        if   request.user.is_staff:
            return True
        if view.action == 'retrieve':
            return request.user.is_authenticated and request.user == view.get_object().visit.patient.user
     

class VisitPermission(BasePermission):
   
    
    def has_permission(self, request, view):
        if   request.user.is_staff:
            return True
        if view.action == 'retrieve':
            return request.user.is_authenticated and request.user == view.get_object().patient.user