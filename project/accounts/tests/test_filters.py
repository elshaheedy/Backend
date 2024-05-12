from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User=get_user_model()
from .test_setup import *
class PatientTestCase(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.staff, self.staff_token = self.create_staff()
        self.patient1, self.patient1_token = self.create_patient(self.staff_token,national_id='11111111111111',full_name='test1')
        self.patient2, self.patient2_token = self.create_patient(self.staff_token,national_id='22222222222222',full_name='test2')
        self.doctor,self.doctor_token = self.create_doctor(self.staff_token,national_id='111111111111171')
        self.visit1 = self.create_visit(self.staff_token,patient_id=self.patient1['id'],start_at='2020-01-01')
        self.visit2 = self.create_visit(self.staff_token,patient_id=self.patient2['id'],start_at='2020-01-02')
    
    def test_get_patient(self):
        url='/accounts/patient/?national_id=11111111111111'
        response = self.client.get(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
     
    def test_get_ordering(self):
        url='/accounts/patient/?ordering=full_name'
        response = self.client.get(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
        patients = response.data['results']
        self.assertEqual(patients[0]['full_name'], 'test1')
        self.assertEqual(patients[1]['full_name'], 'test2')
        url  ='/accounts/patient/?ordering=-full_name'
        response = self.client.get(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
        patients = response.data['results']
        self.assertEqual(patients[0]['full_name'], 'test2')
        self.assertEqual(patients[1]['full_name'], 'test1')