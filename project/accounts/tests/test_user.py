from accounts.tests.test_setup import *
from accounts.models import *
from django.urls import reverse
from rest_framework import status

# class CheckTest(TestSetup):
#     def setUp(self) -> None:
#         super().setUp()
#         self.staff,self.staff_token=self.create_staff(username="12345678901230")
#         self.patient,self.patient_token=self.create_patient(self.staff_token,national_id="1234567890123",email="test@test.com")
#     def test_check_national_id(self):
#         url = reverse('check_national_id')
#         data = {
#             'national_id': '1234567890123'
#         }
#         response = self.client.post(
#             url, data, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data['exists'],True)
#     def test_check_email(self):
#         url = reverse('check_email')
#         data = {
#             'email': 'test@test.com'
#         }
#         response = self.client.post(
#             url, data, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data['exists'],True)


class ChangePasswordTest(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.staff,self.staff_token=self.create_staff()
        self.patient,self.patient_token=self.create_patient(self.staff_token,national_id="12345678901239")
        self.docktor,self.doctor_token=self.create_doctor(self.staff_token,national_id="312345678901239")
        self.url=reverse('change-password')

    def test_change_password(self):
        
        data = {
            'user_id': self.patient['user'],
            'new_password': 'newpassword123'
        }
        response = self.client.post(self.url, data,HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
     
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user=User.objects.get(id=self.patient['user'])
        self.assertTrue(user.check_password('newpassword123'))

    def test_invalid_user_id(self):
        data = {
            'user_id': 9999,
            'new_password': 'newpassword123'
          
        }
        response = self.client.post(self.url, data,HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
     
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_password(self):
        data = {
            'user_id': self.patient['user'],
            # Missing new_password
        }
        response = self.client.post(self.url, data, format='json',HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['new_password'][0], 'This field is required.')

    def test_unauthorized(self):
      
        data = {
            'user_id': self.patient['user'],
            'new_password': 'newpassword123'
        }
        response = self.client.post(self.url, data,HTTP_AUTHORIZATION='Bearer ' + self.patient_token)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    def test_doctor_unauthorized(self):
        data = {
            'user_id': self.patient['user'],
            'new_password': 'newpassword123'
        }
        response = self.client.post(self.url, data,HTTP_AUTHORIZATION='Bearer ' + self.doctor_token)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    def test_doctor_change_his_password(self):
        data = {
            'user_id': self.docktor['user'],
            'new_password': 'newpassword123'
        }
        response = self.client.post(self.url, data,HTTP_AUTHORIZATION='Bearer ' + self.doctor_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)