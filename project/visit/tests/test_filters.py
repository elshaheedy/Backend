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
        self.visit1 = self.create_visit(self.staff_token,patient=self.patient1['id'],start_at='2020-01-01')
        self.visit2 = self.create_visit(self.staff_token,patient=self.patient2['id'],start_at='2020-01-02')
    
    def test_get_visit(self):
        url='/visit/visit/?order_by=created_at'
        response = self.client.get(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
        visit1=response.data['results'][0]
        visit2=response.data['results'][1]
        self.assertEqual(visit1['created_at'] < visit2['created_at'], True)
        url='/visit/visit/?order_by=id'
        response = self.client.get(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
        visit1=response.data['results'][0]
        visit2=response.data['results'][1]
        self.assertEqual(visit1['created_at'] > visit2['created_at'], False)
    def test_get_visit_order_by_start_at(self):
        url='/visit/visit/?order_by=start_at'
        response = self.client.get(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
        visit1=response.data['results'][0]
        visit2=response.data['results'][1]
        self.assertEqual(visit1['start_at'] < visit2['start_at'], True)
        url='/visit/visit/?order_by=-start_at'
        response = self.client.get(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
        visit1=response.data['results'][0]
        visit2=response.data['results'][1]
        self.assertEqual(visit1['start_at'] > visit2['start_at'], False)

    def test_get_visit_start_at_gte(self):
        url='/visit/visit/?start_at__gte=2020-01-02'
        response = self.client.get(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
    def test_get_visit_measurement(self):
        measurement={
            'height': "1cm",
            'weight': "1kg",
            "blood_pressure": "1/1",
            "temperature": "1C",
            "pulse": "1",
            "oxygen_level": "1"
        }
        visit9=self.create_visit(self.staff_token,patient=self.patient1['id'],start_at='2020-01-09',measurement=measurement)
        
        url='/visit/visit/?measurement__height__icontains=1'
        response = self.client.get(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
    