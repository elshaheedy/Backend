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