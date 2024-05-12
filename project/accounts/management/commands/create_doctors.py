# -*- coding: utf-8 -*-
# myapp/management/commands/create_sample_data.py
from itertools import cycle

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from accounts.factories import *

User = get_user_model()


class Command(BaseCommand):
    help = "Populate the database with sample data"

    def handle(self, *args, **options):
        # Create and save sample data for Category

        users_count = max(8-len(Doctor.objects.all()), 0)
        users = UserFactory.create_batch(
            users_count,
        )

        for user in users:
            user.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created and saved {len(users)} users"
            )
        )
    
        Doctors = DoctorFactory.create_batch(
            users_count,
            user=factory.Iterator(cycle(users)),

        )
        for doctor in Doctors:
            doctor.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created and saved {len(Doctors)} doctors"
            )
        )

      