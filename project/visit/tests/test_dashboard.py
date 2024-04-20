from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
class DashboardTest(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_dashboard(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)