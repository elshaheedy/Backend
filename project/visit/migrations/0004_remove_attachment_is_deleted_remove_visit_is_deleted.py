# Generated by Django 5.0.3 on 2024-05-13 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("visit", "0003_attachment_deleted_attachment_deleted_by_cascade_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="attachment",
            name="is_deleted",
        ),
        migrations.RemoveField(
            model_name="visit",
            name="is_deleted",
        ),
    ]
