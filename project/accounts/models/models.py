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
    gender = models.CharField(max_length=255)
    marital_status = models.CharField(max_length=255 ,null=True,blank=True)
    nationality = models.CharField(max_length=255 ,default="Egypt")
    national_id= models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    notes= models.TextField(blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class UserImage(models.Model):
    image = models.ImageField(upload_to='user_images' )
    # user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='user_images' )
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='images' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
class Phone(models.Model):
    mobile = models.CharField(max_length=255)
    # user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='phones' )
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='phones' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    governorate = models.CharField(max_length=255)
    # user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='addresses' )
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='addresses' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.street+" "+self.city

class Patient(Profile):
    disease_type  = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=255)
    code=ShortUUIDField(unique=True, max_length=10,editable=False,blank=True)

    
    
    # def __str__(self):
    #     return self.first_name

class Employee(Profile):
    def __str__(self):
        return self.first_name

class Doctor(Profile):
    speciality = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField()
    work_days= models.CharField(max_length=255)
    
    def __str__(self):
        return self.first_name