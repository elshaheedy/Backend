from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User=get_user_model()
from .test_setup import *
from django.urls import reverse
class PatientDeleteTestCase(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.staff, self.staff_token = self.create_staff()
       

    def test_delete_patient(self):
        patient, patient_token = self.create_patient(self.staff_token,national_id='22222222222222',full_name='test2')

        url='/accounts/patient/{}/'.format(patient['id'])
        response = self.client.delete(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Patient.objects.count(), 0)
        self.assertEqual(len( Patient.deleted_objects.all()), 1)
    def test_delete_patient_hard(self):
        patient, patient_token = self.create_patient(self.staff_token,national_id='22222222222223',full_name='test2')
        self.assertEqual(Patient.objects.count(), 1)
        url='/accounts/patient/{}/?method=hard'.format(patient['id'])
        response = self.client.delete(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
  
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Patient.objects.count(), 0)
        self.assertEqual(len( Patient.deleted_objects.all()), 0)
    def test_delete_patient_restore(self):
        patient, patient_token = self.create_patient(self.staff_token,national_id='22222222222224',full_name='test2')
       
        url='/accounts/patient/{}/'.format(patient['id'])
        response = self.client.delete(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 204)

        data={
            'id':patient['id']
        }
        url=reverse('patient-restore')
        response = self.client.post(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token,data=data)
      
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(len( Patient.deleted_objects.all()), 0)
    def test_delete_patient_get_deleted(self):
        patient, patient_token = self.create_patient(self.staff_token,national_id='22222222222225',full_name='test2')
       
        url='/accounts/patient/{}/'.format(patient['id'])
        response = self.client.delete(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 204)

        url=reverse('patient-get-deleted')
        response = self.client.get(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        # print(response.data)
        self.assertEqual(len(response.data['results']), 1)

class EmployeeDeleteTestCase(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.staff, self.staff_token = self.create_staff()
       

    def test_delete_employee(self):
        employee, employee_token = self.create_employee(self.staff_token,national_id='22222222222222',full_name='test2')

        url='/accounts/employee/{}/'.format(employee['id'])
        response = self.client.delete(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Employee.objects.count(), 0)
        self.assertEqual(len( Employee.deleted_objects.all()), 1)
    def test_delete_employee_hard(self):
        employee, employee_token = self.create_employee(self.staff_token,national_id='22222222222223',full_name='test2')
        self.assertEqual(Employee.objects.count(), 1)
        url='/accounts/employee/{}/?method=hard'.format(employee['id'])
        response = self.client.delete(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
  
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Employee.objects.count(), 0)
        self.assertEqual(len( Employee.deleted_objects.all()), 0)
    def test_delete_employee_restore(self):
        employee, employee_token = self.create_employee(self.staff_token,national_id='22222222222224',full_name='test2')
       
        url='/accounts/employee/{}/'.format(employee['id'])
        response = self.client.delete(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 204)

        data={
            'id':employee['id']
        }
        url=reverse('employee-restore')
        response = self.client.post(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token,data=data)
      
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(len( Employee.deleted_objects.all()), 0)
    def test_delete_employee_get_deleted(self):
        employee, employee_token = self.create_employee(self.staff_token,national_id='22222222222225',full_name='test2')
       
        url='/accounts/employee/{}/'.format(employee['id'])
        response = self.client.delete(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 204)

        url=reverse('employee-get-deleted')
        response = self.client.get(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        # print(response.data)
        self.assertEqual(len(response.data['results']), 1)  



class DoctorDeleteTestCase(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.staff, self.staff_token = self.create_staff()
       

    def test_delete_doctor(self):
        doctor, doctor_token = self.create_doctor(self.staff_token,national_id='22222222222222',full_name='test2')

        url='/accounts/doctor/{}/'.format(doctor['id'])
        response = self.client.delete(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Doctor.objects.count(), 0)
        self.assertEqual(len( Doctor.deleted_objects.all()), 1)
    def test_delete_doctor_hard(self):
        doctor, doctor_token = self.create_doctor(self.staff_token,national_id='22222222222223',full_name='test2')
        self.assertEqual(Doctor.objects.count(), 1)
        url='/accounts/doctor/{}/?method=hard'.format(doctor['id'])
        response = self.client.delete(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
  
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Doctor.objects.count(), 0)
        self.assertEqual(len( Doctor.deleted_objects.all()), 0)
    def test_delete_doctor_restore(self):
        doctor, doctor_token = self.create_doctor(self.staff_token,national_id='22222222222224',full_name='test2')
       
        url='/accounts/doctor/{}/'.format(doctor['id'])
        response = self.client.delete(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 204)

        data={
            'id':doctor['id']
        }
        url=reverse('doctor-restore')
        response = self.client.post(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token,data=data)
        # print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Doctor.objects.count(), 1)
        self.assertEqual(len( Doctor.deleted_objects.all()), 0)
    def test_delete_doctor_get_deleted(self):
        doctor, doctor_token = self.create_doctor(self.staff_token,national_id='22222222222225',full_name='test2')       
        url='/accounts/doctor/{}/'.format(doctor['id'])
        response = self.client.delete(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 204)

        url=reverse('doctor-get-deleted')
        response = self.client.get(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        # print(response.data)
        self.assertEqual(len(response.data['results']), 1)  