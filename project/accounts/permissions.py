# -*- coding: utf-8 -*-
# permissions.py
from rest_framework.permissions import SAFE_METHODS, BasePermission



class StaffPermission(BasePermission):
   

    def has_permission(self, request, view):
        return   request.user.is_staff
     
class OwnPermission(BasePermission):
    def has_permission(self, request, view):
        if   request.user.is_staff:
            return True
        if view.action == 'retrieve':
            return request.user.is_authenticated and request.user == view.get_object().user

        return request.user.is_authenticated    

    def has_object_permission(self, request, view, obj):
        if   request.user.is_staff:
            return True
        if view.action == 'retrieve':
            return request.user.is_authenticated and request.user == view.get_object().user

        return request.user.is_authenticated

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin
        if request.user and request.user.is_superuser:
            return True
        
        if request.method in SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_superuser:
            return True

        if request.method in SAFE_METHODS:
            return True
        return False

            