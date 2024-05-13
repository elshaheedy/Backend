from .models      import *
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
class UserImage(SafeDeleteModel):
    _safedelete_policy =SOFT_DELETE_CASCADE
    image = models.ImageField(upload_to='user_images' )
    # user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='user_images' )
    user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='image' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class Patient(Profile):
    disease_type  = models.CharField(max_length=255,blank=True,null=True)
    blood_type = models.CharField(max_length=255,blank=True,null=True) 
     
