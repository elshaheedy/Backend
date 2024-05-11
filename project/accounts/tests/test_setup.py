# test patient views
from accounts.models import *
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.test import TestCase
from accounts.models import *
from rest_framework.test import APIClient
# from accounts.tests.test_setup import HomeTestSetup


class TestSetup(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
    def get_postion_token(self,postion):
        # user=User.objects.get(username=postion.user.username)
        user=postion.user
        username = user.username
        password = "test123"
        return self.get_token(username, password)

    def get_token(self,username,password):
        token= self.client.post('/accounts/token/', {'username': username, 'password': password}, format='json')
        # if 'access' not in token.data:
            # print('no access',token.data,username,password)
        self.assertEqual(token.status_code, 200)
        return token.data['access']
    def create_staff(self,username='stafftest', password='test123'):
        user=User.objects.create_user(username=username, password=password)
        user.is_superuser = True
        user.save()
        token=self.get_token(username, password)
        return user,token
    
    def create_user(self):
        user = User.objects.create_user(username='test', password='test123')
        return user
    def create_patient(self,staff_token,national_id='01234567890123',
                       email='test1@test.com',
                       full_name='test',
                       date_of_birth='2000-01-01',
                       gender='M',
                       disease_type='test',
                       blood_type='test',
                       marital_status='test',
                       nationality='test',
                       address={
                           'street':'test',
                           'city':'test',
                           'governorate':'test'
                       },
                       phone={
                           'mobile':'test'
                       }
                       
                       ):
   
        data={
     
               'national_id': national_id,
               'email': email,
               'full_name': full_name,
               'date_of_birth': date_of_birth,
               'gender': gender,
               'disease_type': disease_type,
               'blood_type': blood_type,
               'marital_status': marital_status,
               'nationality': nationality,
               'address': address,
               'phone': phone
              



            }   

        response=self.client.post('/accounts/patient/',data,format='json',HTTP_AUTHORIZATION='Bearer ' + staff_token)
        token=self.get_token(data['national_id'], data['national_id'])
        return response.data,token