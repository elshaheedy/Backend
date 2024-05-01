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


def generate_image(file_path):
    if os.path.exists(file_path):
        image_files = [
            f
            for f in os.listdir(file_path)
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
        ]

        # Choose a random image file
        selected_image = random.choice(image_files)

        # Open the selected image file and read its content
        with open(os.path.join(file_path, selected_image), "rb") as file:
            image_content = file.read()

        # Return a SimpleUploadedFile with the selected image content
        return SimpleUploadedFile(selected_image, image_content)

    # Create a simple random image using Pillow
    image = Image.new("RGB", (100, 100), "rgb(255, 0, 0)")
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    return SimpleUploadedFile("image.jpg", buffer.getvalue())


def generate_user_image():
    return generate_image(file_path="test_data/images/products")





class PatientCodeProvider(BaseProvider):
    def product_code(self):
        # Generate your product code logic here
        return "PROD" + "".join(str(random.randint(0, 9)) for _ in range(6))

class PatientNationalityProvider(BaseProvider):
    def  patient_national_id(self):
        # Generate your product code logic here
        return  "".join(str(random.randint(0, 9)) for _ in range(14))
class PatientNameProvider(BaseProvider):
    def  patient_name(self):
        arabic_mens_names = [
            "محمد", "علي", "أحمد", "عمر", "يوسف",
            "خالد", "حسن", "مصطفى", "حسام", "محمود",
            "سعيد", "طارق", "عبد الله", "عليّ", "ماجد",
            "جمال", "وليد", "مروان", "ناصر", "رشيد",
            "حسين", "سليمان", "عبدالرحمن", "فارس", "ياسر",
            "عليان", "رامي", "خضر", "طلال",
            "حازم", "إياد", "أسامة", "أمين", "منصور",
            "مالك", "نواف", "أكرم", "شريف", "أيمن"
        ]

        arabic_names = [ "نور", "إحسان","جهاد",",وسام","اسلام"]



        last=" ".join(random.choice(arabic_mens_names) for _ in range(3))
        first=random.choice(arabic_names)
        return first+" "+last
class AddressStreetProvider(BaseProvider):
    def  street_name(self):
        egyptian_village_names = [
            "الدلجا",
            "كفر الشيخ",
            "بركة السبع",
            "قلوص",
            "الشهداء",
            "سمسطا",
            "دمنهور",
            "كفر الشيخ الجديدة",
            "بدر",
            "برمبال",
            "كفر المنجوم",
            "النوبارية",
            "الرياض",
            "البيضاء",
            "الرزايقة",
            "قرية النيل",
            "دسوق",
            "كفر البطيخ",
            "أبو النمرس",
            "أبو حمص"
        ]

        return random.choice(egyptian_village_names)
class AddressCityProvider(BaseProvider):
    def  city(self):
        egyptian_village_names = [
            "الدلجا",
            "كفر الشيخ",
            "بركة السبع",
            "قلوص",
            "الشهداء",
            "سمسطا",
            "دمنهور",
            "كفر الشيخ الجديدة",
            "بدر",
            "برمبال",
            "كفر المنجوم",
            "النوبارية",
            "الرياض",
            "البيضاء",
            "الرزايقة",
            "قرية النيل",
            "دسوق",
            "كفر البطيخ",
            "أبو النمرس",
            "أبو حمص"
        ]

        return random.choice(egyptian_village_names)

class AddressGovernorateProvider(BaseProvider):
    def  state(self):
        egyptian_village_names = [
            "الدلجا",
            "كفر الشيخ",
            "بركة السبع",
            "قلوص",
            "الشهداء",
            "سمسطا",
            "دمنهور",
            "كفر الشيخ الجديدة",
            "بدر",
            "برمبال",
            "كفر المنجوم",
            "النوبارية",
            "الرياض",
            "البيضاء",
            "الرزايقة",
            "قرية النيل",
            "دسوق",
            "كفر البطيخ",
            "أبو النمرس",
            "أبو حمص"
        ]

        return random.choice(egyptian_village_names)
    

factory.Faker.add_provider(PatientCodeProvider)
factory.Faker.add_provider(PatientNationalityProvider)
factory.Faker.add_provider(PatientNameProvider)
factory.Faker.add_provider(AddressStreetProvider)
factory.Faker.add_provider(AddressCityProvider)
factory.Faker.add_provider(AddressGovernorateProvider)
class PatientFactory(factory.Factory):
    class Meta:
        model = Patient
    full_name = factory.Faker( "patient_name")
    national_id = factory.Faker("patient_national_id")
    date_of_birth = factory.Faker("date")
    gender = factory.Faker("random_element", elements=["M", "F"])
    blood_type = factory.Faker("random_element", elements=["A", "B", "AB", "O"])
    disease_type = factory.Faker("word")
    marital_status = factory.Faker("word")
    nationality = factory.Faker("word")

class AddressFactory(factory.Factory):
    class Meta:
        model = Address
    street = factory.Faker("street_name")
    city = factory.Faker("city")
    governorate = factory.Faker("state")
class PhoneFactory(factory.Factory):
    class Meta:
        model = Phone
    mobile = factory.Faker("phone_number")
class UserImageFactory(factory.Factory):
    class Meta:
        model = UserImage
    image = factory.django.ImageField(color="blue")

class UserFactory(factory.Factory):
    class Meta:
        model = User
    username = factory.Faker("patient_national_id")
    password = factory.Faker("patient_national_id")
  