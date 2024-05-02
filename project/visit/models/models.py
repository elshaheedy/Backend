from django.db import models

# Create your models here.
class Visit(models.Model):
    id = models.AutoField(primary_key=True)
    visit_number = models.IntegerField(null=True)
    ticket = models.CharField(max_length=255)
    doctors = models.ManyToManyField('accounts.Doctor',null=True ,blank=True , related_name='visits')
    # date = models.DateField()
    # time = models.TimeField()
    datatime = models.DateTimeField(auto_now_add=True)
    # enddatetime = models.DateTimeField(null=True)

    patient = models.ForeignKey('accounts.Patient', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    def save(self, *args, **kwargs):
        self.visit_number = Visit.objects.count()+1
        super(Visit, self).save(*args, **kwargs)
class Measurement(models.Model):
    visit = models.ForeignKey('visit.Visit', on_delete=models.CASCADE)
    height = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    blood_pressure = models.CharField(max_length=255)
    temperature = models.CharField(max_length=255)
    pulse = models.CharField(max_length=255)
    oxygen_level = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

class Attachment(models.Model):
    visit = models.ForeignKey('visit.Visit', on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments')
    kind = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)