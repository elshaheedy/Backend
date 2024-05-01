from accounts.tests.test_setup import *
from accounts.models import *


class AddressTest(PostionTestSetup):
    def setUp(self) -> None:
        super().setUp()
        self.url = '/accounts/address/'
        self.staff, self.staff_token = self.create_staff()
        self.patient, self.patient_token = self.create_patient(
            self.staff_token)

    def test_get_address(self):
        response = self.client.get(
            self.url+f'{self.patient["id"]}/', format='json', HTTP_AUTHORIZATION='Bearer ' + self.staff_token)
        self.assertEqual(response.status_code, 200)
        print(response.data)


