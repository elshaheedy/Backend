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

class PatientReqTest(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.staff, self.staff_token = self.create_staff()
        self.patient, self.patient_token = self.create_patient(
            self.staff_token)
    def test_create_patient(self):
        data = {
  
               
                'national_id': '012345678901234',
                'full_name': 'test',
            


        }

        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        response = self.client.post('/accounts/patient/', data,
                                    format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 201)

        self.assertEqual(Patient.objects.get(
            national_id='012345678901234').full_name, 'test')
        self.assertEqual(response.data['full_name'], 'test')
      