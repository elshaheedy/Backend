from .models      import *
class Doctor(Profile):
    speciality = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255,blank=True,null=True)
    experience_years = models.PositiveIntegerField( blank=True, null=True)
    work_days= models.CharField(max_length=255,blank=True,null=True)
    
    # def __str__(self):
    #     return self.first_name