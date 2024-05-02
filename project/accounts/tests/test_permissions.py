from accounts.tests.test_setup import *
from accounts.models import *
from django.urls import reverse
class PermissionTest(PostionTestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.url = '/accounts/permission/'
        self.staff, self.staff_token = self.create_staff()
        self.patient, self.patient_token = self.create_patient(
            self.staff_token)
    def test_list_permission_superuser(self):
        response = self.client.get(
            self.url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
    def test_list_permission_patient(self):
        response = self.client.get(
            self.url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.patient_token)
        self.assertEqual(response.status_code, 403)
    
    def  test_assign_permissions_to_user(self):
        permissions = self.client.get(
            self.url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token).data
       
        # url=reverse('assign-permissions-to-user')
        user = User.objects.create_user(username='testpermission', password='test123')
        # url=reverse('user-details', args=[user.id])
        url = reverse('user-details-detail', kwargs={'pk': user.id})

        permission_ids = [permission['id'] for permission in permissions]
        data = {
             'user_permissions' : [ permission_ids[0], permission_ids[1] ]
        }
        response = self.client.patch(
            url, data, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            url, format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        # print(response.data)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data['user_permissions']), 2)
