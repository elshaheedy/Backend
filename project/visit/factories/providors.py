
import random
import factory
from faker.providers import BaseProvider




class MedicalRecordProvider(BaseProvider):
    def  medical_record(self):
        return {
            "blood_pressure":  "".join(str(random.randint(0, 9)) for _ in range(2)),
            "temperature":  "".join(str(random.randint(0, 9)) for _ in range(2)),
            "pulse":  "".join(str(random.randint(0, 9)) for _ in range(2)),
            "oxygen_level":  "".join(str(random.randint(0, 9)) for _ in range(2)),
            "height":  "1"+"".join(str(random.randint(0, 9)) for _ in range(2)),
            "weight":  "1"+"".join(str(random.randint(0, 9)) for _ in range(2)),
        }

factory.Faker.add_provider(MedicalRecordProvider)
