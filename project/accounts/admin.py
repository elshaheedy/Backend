"""
Module for administration configurations.

This module contains the administration configurations for the accounts app.
"""
# Your admin configurations follow here
from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from .models import *

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Employee)
admin.site.register(UserImage)
