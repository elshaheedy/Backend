"""
Module for administration configurations.

This module contains the administration configurations for the accounts app.
"""
# Your admin configurations follow here
from django.contrib import admin

from .models import *

admin.site.register(Patient)
admin.site.register(Phone)
admin.site.register(Address)
admin.site.register(Doctor)
admin.site.register(Employee)
