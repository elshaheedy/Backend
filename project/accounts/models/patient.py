from .models      import *
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE



class Patient(Profile):
    disease_type  = models.CharField(max_length=255,blank=True,null=True)
    blood_type = models.CharField(max_length=255,blank=True,null=True) 
     
