from accounts.tests.test_setup import *
from accounts.models import *

from accounts.tests.test_setup import *
from accounts.models import *



class PatientTest(TestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.staff, self.staff_token = self.create_staff()
      
    def test_create_doctor(self):
        data = {
  
                
                'national_id': '012345678901234',
                'full_name': 'test',
            


        }

        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        response = self.client.post('/accounts/doctor/', data,
                                    format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Doctor.objects.count(), 0)
        self.assertEqual(User.objects.count(), 1)


