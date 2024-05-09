from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Visit)
admin.site.register(models.Attachment)