"""
Module for application configuration.

This module contains the configuration class for the accounts app.
"""
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuration class for the accounts app.

    This class represents the configuration for the accounts app in the Django project.
    It provides settings and initialization logic specific to the accounts app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
