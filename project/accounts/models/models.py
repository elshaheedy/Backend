"""
Module for defining database models.

This module contains the database models for the accounts app.
"""
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from shortuuidfield import ShortUUIDField

User=get_user_model()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , null=True )
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True, null=True)
    gender = models.CharField(max_length=255, null=True,blank=True)
    marital_status = models.CharField(max_length=255 ,null=True,blank=True)
    nationality = models.CharField(max_length=255 ,default="Egypt")
    national_id= models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    notes= models.TextField(blank=True,null=True)
    address = models.JSONField(null=True, blank=True)
    phone = models.JSONField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


    
