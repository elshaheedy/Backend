# -*- coding: utf-8 -*-
# myapp/factories.py
import io
import os
import random

import factory
from django.core.files.uploadedfile import SimpleUploadedFile
from faker import Faker
from faker.providers import BaseProvider
from PIL import Image
from accounts.models import *

fake = Faker()

from.providors import *

from .utls import generate_user_image



class PatientFactory(factory.Factory):
    class Meta:
        model = Patient
    full_name = factory.Faker( "arabic_name")
    national_id = factory.Faker("national_id")
    date_of_birth = factory.Faker("date")
    gender = factory.Faker("random_element", elements=["M", "F"])
    blood_type = factory.Faker("random_element", elements=["A", "B", "AB", "O"])
    disease_type = factory.Faker("word")
    marital_status = factory.Faker("word")
    nationality = factory.Faker("word")
    address=factory.Faker("address")
    phone=factory.Faker("phone")



class UserImageFactory(factory.Factory):
    class Meta:
        model = UserImage
    image = factory.django.ImageField(color="blue")

class UserFactory(factory.Factory):
    class Meta:
        model = User
    username = factory.Faker("national_id")
    password = factory.Faker("national_id")
  
class DoctorFactory(factory.Factory):
    class Meta:
        model = Doctor
    full_name = factory.Faker( "arabic_name")
    national_id = factory.Faker("national_id")
    date_of_birth = factory.Faker("date")
    gender = factory.Faker("random_element", elements=["M", "F"])
    marital_status = factory.Faker("word")

    speciality = factory.Faker("doctor_specialization")
    license_number = factory.Faker("random_digit")
    experience_years = factory.Faker("random_digit")
    work_days = factory.Faker("week_days")


 

