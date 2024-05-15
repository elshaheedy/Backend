

from rest_framework import serializers
from visit.models import *

    
class AttachmentSerializer(serializers.ModelSerializer):
    file_type=serializers.CharField(read_only=True)
    class Meta:
        model = Attachment
        fields = '__all__'

class RestoreAttachmentSerializer(serializers.Serializer):
    id = serializers.CharField()
    def validate_id(self, value):
        try:
            attachment = Attachment.deleted_objects.get(id=value)
        except Attachment.DoesNotExist:
            raise serializers.ValidationError("Attachment does not exist.")
        return attachment