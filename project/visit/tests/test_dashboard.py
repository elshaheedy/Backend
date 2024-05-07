from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .test_setup import *
class DashboardTest(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_dashboard(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)




class StatisticsViewTestCase(TestSetup):
    def setUp(self):
        super().setUp()
        # Create test data
        self.staff, self.staff_token = self.create_staff()
        self.patient1, self.patient1_token = self.create_patient(self.staff_token,national_id='11111111111111')
        self.patient2, self.patient2_token = self.create_patient(self.staff_token,national_id='22222222222222')
        self.visit1 = self.create_visit(self.staff_token,patient=self.patient1['id'])
        self.visit2 = self.create_visit(self.staff_token,patient=self.patient2['id'])


    def test_patient_filter(self):

        response = self.client.get('/visit/statistics/?patient_', format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
