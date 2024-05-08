from .models      import *
class Doctor(Profile):
    speciality = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField()
    work_days= models.CharField(max_length=255)
    
    def __str__(self):
        return self.first_name