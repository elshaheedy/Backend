from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User=get_user_model()
from .test_setup import *
class VisitTestCase(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.staff, self.staff_token = self.create_staff()
        self.patient1, self.patient1_token = self.create_patient(self.staff_token,national_id='11111111111111')
        self.patient2, self.patient2_token = self.create_patient(self.staff_token,national_id='22222222222222')
        self.doctor,self.doctor_token = self.create_doctor(self.staff_token,national_id='111111111111171')
        self.visit1 = self.create_visit(self.staff_token,patient=self.patient1['id'])
        self.visit2 = self.create_visit(self.staff_token,patient=self.patient2['id'])
    def test_create_visit(self):

        data = {
            'patient': self.patient1['id'],
            'ticket': '2',
            'doctors': [self.doctor['id']]
        }
        response = self.client.post('/visit/visit/', data, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.data['doctors']), 1)
    def test_update_visit(self):
        data = {
            'patient': self.patient1['id'],
            'ticket': '2',
            'measurement':{
                'height': 100,
                'weight': 100,
                'blood_pressure': 100,
                'temperature': 100,
                'pulse': 100,
                'oxygen_level': 100
            }
            
        }
        response = self.client.put('/visit/visit/'+str(self.visit1['id'])+'/', data, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['ticket'], '2')
        self.assertEqual(response.data['measurement']['height'], '100')
    def test_delete_visit(self):
        response = self.client.delete('/visit/visit/'+str(self.visit1['id'])+'/', format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 204)
    def test_get_visit(self):
        response = self.client.get('/visit/visit/'+str(self.visit1['id'])+'/', format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)