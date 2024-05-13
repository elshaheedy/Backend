from re import S
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
class Visit(SafeDeleteModel):

    _safedelete_policy =SOFT_DELETE_CASCADE

    status = models.CharField(max_length=255, null=True, blank=True,
                               choices=[('pending', 'Pending'),('done', 'Done'),('canceled', 'Canceled')])

    visit_number = models.IntegerField(null=True)
    ticket = models.CharField(max_length=255)
    doctors = models.ManyToManyField('accounts.Doctor',null=True ,blank=True , related_name='visits')
    measurement=models.JSONField(null=True,blank=True)
    start_at= models.DateTimeField(null=True)
    end_at = models.DateTimeField(null=True)
    patient = models.ForeignKey('accounts.Patient', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    def save(self, *args, **kwargs):
        self.visit_number = Visit.objects.count()+1
        super(Visit, self).save(*args, **kwargs)


class Attachment(SafeDeleteModel):

    _safedelete_policy =SOFT_DELETE_CASCADE
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_attachments', null=True, blank=True)
    visit = models.ForeignKey('visit.Visit', on_delete=models.CASCADE, related_name='visit_attachments', null=True, blank=True)
    kind = models.CharField(max_length=255)
    
    file_name = models.CharField(max_length=255, null=True, blank=True) 
    file_type = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to='attachments')

    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        self.file_type = self.file.name.split('.')[-1]
        super(Attachment, self).save(*args, **kwargs)

