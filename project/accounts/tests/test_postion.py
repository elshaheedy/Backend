from django.test import TestCase, override_settings
from io import BytesIO
from PIL import Image
import os
from accounts.tests.test_setup import *
from accounts.models import *
from unittest.mock import patch
from django.core.files.uploadedfile import SimpleUploadedFile


class PostionTest(PostionTestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.staff, self.staff_token = self.create_staff()
        self.patient, self.patient_token = self.create_patient(
            self.staff_token)

    def test_create_patient(self):
        data = {
            'patient': {
                'marital_status': 'test',
                'nationality': 'test',
                'full_name': 'test',
                'national_id': '012345678901234',
                'date_of_birth': '2000-01-01',
                'gender': 'M',
                'disease_type': 'test',
                'blood_type': 'test',
                'address': {
                    'street': 'test',
                    'city': 'test',
                    'governorate': 'test'
                },
                'phone': {
                    'mobile': 'test'
                }
            },


        }

        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        response = self.client.post('/accounts/postion-create/', data,
                                    format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        # print("response",response.data)
        self.assertEqual(response.status_code, 201)

        self.assertEqual(Patient.objects.get(
            national_id='012345678901234').full_name, 'test')
        self.assertEqual(response.data['patient']['full_name'], 'test')
        self.assertEqual(response.data['patient']['address']['city'], 'test')

    def test_update_patient(self):

        url = f'/accounts/home-update/'
        data = {


            'patient': {
                'id': self.patient['id'],
                'marital_status': 'test',
                'nationality': 'test',
                'full_name': 'test2',
                'national_id': '01234567890123',
                'date_of_birth': '2000-01-01',
                'gender': 'M',
                'disease_type': 'test',
                'blood_type': 'test',
                'address': {
                    'id': Address.objects.get(user=self.patient['user']).id,
                    'street': 'test',
                    'city': 'test2',
                    'governorate': 'test'
                },
                'phone': {
                    'id': Phone.objects.get(user=self.patient['user']).id,
                    'mobile': 'test'
                }
            },


        }

        response = self.client.post('/accounts/postion-update/', data,
                                    format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['patient']['full_name'], 'test2')
        self.assertEqual(response.data['patient']['address']['city'], 'test2')


class PostionPermissionTest(PostionTestSetup):
    def setUp(self) -> None:
        super().setUp()

        self.staff, self.staff_token = self.create_staff()
        self.patient, self.patient_token = self.create_patient(
            self.staff_token)

    def test_create_patient(self):
        data = {
            'patient': {
                'marital_status': 'test',
                'nationality': 'test',
                'full_name': 'test',
                'national_id': '012345678901234',
                'date_of_birth': '2000-01-01',
                'gender': 'M',
                'disease_type': 'test',
                'blood_type': 'test',
                'address': {
                    'street': 'test',
                    'city': 'test',
                    'governorate': 'test'
                },
                'phone': {
                    'mobile': 'test'
                }
            },


        }
        url = '/accounts/postion-create/'
        response = self.client.post(url, data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, 401)

        response = self.client.post(
            url, data, format='json', HTTP_AUTHORIZATION='Bearer ' + self.patient_token)
        self.assertEqual(response.status_code, 403)

        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        response = self.client.post(
            url, data, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['patient']['full_name'], 'test')
        self.assertEqual(response.data['patient']['address']['street'], 'test')

        # self.assertEqual(Patient.objects.get(national_id='012345678901234').full_name, 'test')

    def test_update_patient(self):

        url = f'/accounts/postion-update/'
        data = {


            'patient': {
                'id': self.patient['id'],
                'marital_status': 'test',
                'nationality': 'test',
                'full_name': 'test2',
                'national_id': '01234567890123',
                'date_of_birth': '2000-01-01',
                'gender': 'M',
                'disease_type': 'test',
                'blood_type': 'test',
                # 'image': None,
                'address': {
                    'id': Address.objects.get(user=self.patient['user']).id,
                    'street': 'test',
                    'city': 'test2',
                    'governorate': 'test'
                },
                'phone': {
                    'id': Phone.objects.get(user=self.patient['user']).id,
                    'mobile': 'test'
                }

            },

        }

        url = f'/accounts/postion-update/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 401)

        response = self.client.post(
            url, data, format='json', HTTP_AUTHORIZATION='Bearer ' + self.patient_token)
        self.assertEqual(response.status_code, 403)

        response = self.client.post(
            url, data, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['patient']['full_name'], 'test2')
        self.assertEqual(response.data['patient']['address']['city'], 'test2')


def create_image_test():
    if os.path.exists("test_image.jpg"):
        return
    from PIL import Image, ImageDraw

    image = Image.new("RGB", (200, 200), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle([(50, 50), (150, 150)], fill="red")
    image.save("test_image.jpg")
    image.show()


class PostionWithImageTest(PostionTestSetup):
    def setUp(self) -> None:
        super().setUp()

        self.staff, self.staff_token = self.create_staff()
        self.patient, self.patient_token = self.create_patient(
            self.staff_token)

    @override_settings(MEDIA_ROOT='/tmp/')  # Override media root for testing
    def test_create_patient(self):
        user = User.objects.create_user(username='test', password='test123')
      
        if not os.path.exists("test_image.jpg"):
            create_image_test()

        with open("test_image.jpg", "rb") as img:

            obj = {
                "user": user.id,
                "image": SimpleUploadedFile(
                    "test_image.jpg", img.read(), content_type="image/jpeg"
                ),

            }

        url = '/accounts/user-image/'

        response = self.client.post(
            url, obj, HTTP_AUTHORIZATION='Bearer ' + self.staff_token )

        self.assertEqual(response.status_code, 201)
        # remvove image
        os.remove("test_image.jpg")