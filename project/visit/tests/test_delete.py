from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User=get_user_model()
from .test_setup import *
from visit.models import *
from django.urls import reverse
class VisitTestCase(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.staff, self.staff_token = self.create_staff()
        self.patient1, self.patient1_token = self.create_patient(self.staff_token,national_id='11111111111111')
        self.patient2, self.patient2_token = self.create_patient(self.staff_token,national_id='22222222222222')
        self.doctor,self.doctor_token = self.create_doctor(self.staff_token,national_id='111111111111171')
        self.visit1 = self.create_visit(self.staff_token,patient=self.patient1['id'],start_at='2020-01-01')
        self.visit2 = self.create_visit(self.staff_token,patient=self.patient2['id'],start_at='2020-01-02')
    
    def test_delete_visit(self):
        url=f'/visit/visit/{self.visit1["id"]}/'
        response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 204)
        url=f'/visit/visit/{self.visit1["id"]}/'
        response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Visit.objects.count(), 1)
        self.assertEqual(Visit.deleted_objects.count(), 1)
    def test_delete_visit_hard(self):
        url=f'/visit/visit/{self.visit1["id"]}/?method=hard'
        response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 204)
        url=f'/visit/visit/{self.visit1["id"]}/?method=hard'
        response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Visit.objects.count(), 1)
        self.assertEqual(Visit.deleted_objects.count(), 0)
    def test_delete_visit_restore(self):
        url=f'/visit/visit/{self.visit1["id"]}/?method=soft'
        response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 204)
        # url=reverse('visit-restore',)
        url=f"/visit/deleted-visit/restore/{self.visit1['id']}/"

        response = self.client.post(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Visit.objects.count(), 2)
        self.assertEqual(Visit.deleted_objects.count(), 0)
    def test_delete_visit_get_deleted(self):
        url=f'/visit/visit/{self.visit1["id"]}/?method=soft'
        response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 204)
        url=f'/visit/visit/deleted/'
        response = self.client.get(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)



# class AttachmentTestCase(TestSetup):
#     def setUp(self) -> None:
#         super().setUp()
#         self.staff, self.staff_token = self.create_staff()
#         self.patient1, self.patient1_token = self.create_patient(self.staff_token,national_id='11111111111111')
#         self.patient2, self.patient2_token = self.create_patient(self.staff_token,national_id='22222222222222')
#         self.doctor,self.doctor_token = self.create_doctor(self.staff_token,national_id='111111111111171')
#         self.visit1 = self.create_visit(self.staff_token,patient=self.patient1['id'],start_at='2020-01-01')
#         self.visit2 = self.create_visit(self.staff_token,patient=self.patient2['id'],start_at='2020-01-02')
#         self.attachment1 = self.create_attachment(self.staff_token,visit=self.visit1['id'],file='test.txt')
#         self.attachment2 = self.create_attachment(self.staff_token,visit=self.visit2['id'],file='test.txt')

#     def test_delete_attachment(self):
#         url=f'/visit/attachment/{self.attachment1["id"]}/'
#         response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
#         self.assertEqual(response.status_code, 204)
#         url=f'/visit/attachment/{self.attachment1["id"]}/'
#         response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
#         self.assertEqual(response.status_code, 404)
#         self.assertEqual(Attachment.objects.count(), 1) 
#         self.assertEqual(Attachment.deleted_objects.count(), 1) 
#     def test_delete_attachment_hard(self):
#         url=f'/visit/attachment/{self.attachment1["id"]}/?method=hard'
#         response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
#         self.assertEqual(response.status_code, 204)
#         url=f'/visit/attachment/{self.attachment1["id"]}/?method=hard'
#         response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
#         self.assertEqual(response.status_code, 404)
#         self.assertEqual(Attachment.objects.count(), 1) 
#         self.assertEqual(Attachment.deleted_objects.count(), 0) 
#     def test_delete_attachment_restore(self):
#         url=f'/visit/attachment/{self.attachment1["id"]}/?method=soft'
#         response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
#         self.assertEqual(response.status_code, 204)
#         url=reverse('attachment-restore')
#         data={
#             'id':self.attachment1['id']
#         }
#         response = self.client.post(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token,data=data)

#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(Attachment.objects.count(), 2)
#         self.assertEqual(Attachment.deleted_objects.count(), 0)
#     def test_delete_attachment_get_deleted(self):
#         url=f'/visit/attachment/{self.attachment1["id"]}/?method=soft'
#         response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
#         self.assertEqual(response.status_code, 204)
#         url=f'/visit/attachments/deleted/'
#         response = self.client.get(url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data['results']), 1)