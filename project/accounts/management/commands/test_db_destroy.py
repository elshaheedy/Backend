# project/app_name/management/commands/test_db_destroy.py

from django.core.management.base import BaseCommand
from django.db import connections

class Command(BaseCommand):
    help = 'Destroy the test database'

    def handle(self, *args, **options):
        connection = connections['default']
        cursor = connection.cursor()
        cursor.execute('DROP DATABASE IF EXISTS test_hospital')
        self.stdout.write(self.style.SUCCESS('Test database destroyed successfully.'))
        print("Test database destroyed successfully.")