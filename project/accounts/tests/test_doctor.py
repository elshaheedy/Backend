from accounts.tests.test_setup import *
from accounts.models import *



from django.test import TestCase, override_settings
from io import BytesIO
from PIL import Image
import os
from accounts.tests.test_setup import *
from accounts.models import *
from unittest.mock import patch
from django.core.files.uploadedfile import SimpleUploadedFile


class DoctorTest(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.staff, self.staff_token = self.create_staff()
        self.patient, self.patient_token = self.create_patient(
                self.staff_token,national_id="123456789000")
        # self.doctor,self.doctor_token=self.create_doctor(self.staff_token)
    def test_create_patient(self):
        data = {
  
                'marital_status': 'test',
                'nationality': 'test',
                'full_name': 'test',
                'national_id': '123456789000',
                'date_of_birth': '2000-01-01',
                'gender': 'M',
                'disease_type': 'test',
                'blood_type': 'test',
                'address': {
                    'street': 'test',
                    'city': 'test',
                    'governorate': 'test'
                },
                'phone': {
                    'mobile': 'test'
                }
            


        }

        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        # response = self.client.post('/accounts/patient/', data,
        #                             format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        # self.assertEqual(response.status_code, 201)
        # response = self.client.post('/accounts/patient/', data,
        #                 format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        # self.assertEqual(response.status_code, 400)

