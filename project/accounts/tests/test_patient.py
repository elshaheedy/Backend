from accounts.tests.test_setup import HomeTestSetup
from accounts.models import *


class HomeTest(HomeTestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.url = '/accounts/patient/'
        self.staff, self.staff_token = self.create_staff()
        self.patient, self.patient_token = self.create_patient(
            self.staff_token)

    def test_create_patient(self):
        data = {
            'marital_status': 'test',
            'nationality': 'test',
            'full_name': 'test',
            'national_id': '0123456789012342',
            'date_of_birth': '2000-01-01',
            'gender': 'M',
            'disease_type': 'test',
            'blood_type': 'test',
        }

        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        response = self.client.post(
            self.url, data, format='json', HTTP_AUTHORIZATION='Bearer ' + self.patient_token)
        self.assertEqual(response.status_code, 403)
    def test_list_patients(self):
        response = self.client.get(
            self.url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.patient_token)
        self.assertEqual(response.status_code, 403)
    def test_get_patient(self):
        response = self.client.get(
            self.url+f'{self.patient["id"]}/', format='json', HTTP_AUTHORIZATION='Bearer ' + self.patient_token)
        self.assertEqual(response.status_code, 200)
