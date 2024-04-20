# from django.test import TestCase
# from rest_framework.test import APIClient
# from django.contrib.auth import get_user_model
# User=get_user_model()
# class VisitTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.url='/visit/visit/'
#         patient_data={
#             'patient':{

            
#             'full_name': 'test',
#             'email': 'test',
#             'gender': 'M',
#             'marital_status': 'test',
#             'nationality': 'test',
#             'national_id': 'test',
#             'date_of_birth': '2000-01-01',
#             'gender': 'M',
#             'notes': 'test',
#             'blood_type': 'test',
#             'disease_type': 'test',

#             }
#         }
#         self.patient = self.client.post('/accounts/patient/', patient_data, format='json').data
#         self.user=User.objects.get(username='test')
#         self.user.is_staff = True
#         self.user.save()
#         self.token = self.client.post('/accounts/token/', {'username': 'test', 'password': 'test'}).data['access']
        
#         # doctor_data={
#         #     'full_name': 'test',
#         #     'email': 'test',
#         #     'gender': 'M',
#         #     'marital_status': 'test',
#         #     'nationality': 'test',
#         #     'national_id': 'test',
#         #     'date_of_birth': '2000-01-01',
#         #     'gender': 'M',
#         #     'notes': 'test',
#         # }
#         # doctor = self.client.post('/accounts/doctor/', doctor_data, format='json').data
#     def test_visit(self):
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
#         data={
#             'visit':
#             {
#                 'patient':self.patient['patient']['id'],
#                 'doctor':'test',
#                 'date':'2000-01-01',
#                 'time':'12:00:00',
#                 'notes':'test',
#                 'ticket':'test',

#             },
           
#            'mesurement':
#             {
#                 'height':'test',
#                 'weight':'test',
#                 'blood_pressure':'test',
#                 'temperature':'test',
#                 'pulse':'test',
#                 'oxygen_level':'test',
#             }

#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, 201)
