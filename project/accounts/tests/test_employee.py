from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

User=get_user_model()
class AuthTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
    def test_signup(self):
        url = '/accounts/signup/'
        data = {
            'username': 'test',
            'password': 'test',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
    def test_login(self):
        '''
        create user first
        '''
        url = '/accounts/signup/'
        data = {
            'username': 'test',
            'password': 'test',
        }
        response = self.client.post(url, data, format='json')
        '''
        test login
        '''
        url = '/accounts/token/'
        data = {
            'username': 'test',
            'password': 'test',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access',response.data)
        self.assertIn('user',response.data)
    def test_creaet_employee(self):
        url = '/accounts/signup/'
        data = {
            'username': 'test',
            'password': 'test',
        }
        response = self.client.post(url, data, format='json')
        url = '/accounts/employee/'
        data = {
            'user': response.data['user']['id'],
            'first_name': 'test',
            'last_name': 'test',
            'date_of_birth': '2000-01-01',
            'gender': 'M',

        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
