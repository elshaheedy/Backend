'''
from django.db import models

# Create your models here.
Visit
   
Measurement

class Attachment(models.Model):

'''

from rest_framework import serializers
from .models import *
class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        # fields = '__all__'
        exclude = ['is_deleted']
    def to_representation(self, instance):
        data= super().to_representation(instance)
        messurement=Measurement.objects.filter(visit=data['id'])
        data['measurement']=MeasurementSerializer(messurement,many=True).data
        attachment=Attachment.objects.filter(visit=data['id'])
        data['attachment']=AttachmentSerializer(attachment,many=True).data
        return data
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        # fields = '__all__'
        exclude = ['is_deleted']
class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        # fields = '__all__'
        exclude = ['is_deleted']

class StatisticsSerializer(serializers.Serializer):
    total_visits=serializers.IntegerField()
    total_patients=serializers.IntegerField()
    total_doctors=serializers.IntegerField()
    total_employees=serializers.IntegerField()