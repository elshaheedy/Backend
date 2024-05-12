import factory
from visit.models import Visit

class MedicalRecordFactory(factory.Factory):
    blood_pressure = factory.Faker("word")  
    oxygen_level = factory.Faker("word")
    temperature = factory.Faker("word")
    height = factory.Faker("word")
    weight = factory.Faker("word")
    pulse = factory.Faker("word")
class VisitFactory(factory.Factory):
    class Meta:
        model = Visit
        exclude = ['is_deleted']
    ticket = factory.Faker("word")
    patient = factory.SubFactory("accounts.factories.PatientFactory")
    # doctors = factory.SubFactory("accounts.factories.DoctorFactory")
    measurement = factory.SubFactory("visit.factories.MedicalRecordFactory")
class AttachmentFactory(factory.Factory):
    class Meta:
        model = Visit
        exclude = ['is_deleted']
    user = factory.SubFactory("accounts.factories.UserFactory")
    visit = factory.SubFactory("visit.factories.VisitFactory")
    file = factory.django.FileField(from_path="/home/mohamed/documents/programming/project_djnago/Hospital-Backend/old/EE_PControl_Lec1.pdf")
