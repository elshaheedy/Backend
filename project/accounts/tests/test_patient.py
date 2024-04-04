# test patient views
from accounts.models import *
from django.test import TestCase
from rest_framework.test import APIClient


class PatientTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_patient(self):
        url='/accounts/patient/'
        # url=reverse('patient-create')
        data={


            'first_name':'test',
            'last_name':'test',
            'date_of_birth':'2000-01-01',
            'gender':'M',
            'disease_type':'test',
            'blood_type':'test'

        }
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(Patient.objects.get().first_name, 'test')


