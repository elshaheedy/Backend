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

        users_count = max(13-len(Patient.objects.all()), 0)
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
        # users_count=len(User.objects.all())
        # users = User.objects.all()

        Patients = PatientFactory.create_batch(
            users_count,
            user=factory.Iterator(cycle(users)),

        )
        for patient in Patients:
            patient.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created and saved {len(Patients)} patients"
            )
        )

        images = UserImageFactory.create_batch(
            users_count,
            user=factory.Iterator(cycle(users)),
        )

        for image in images:
            image.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created and saved {len(images)} images")
        )

        # addresses = AddressFactory.create_batch(
        #     users_count,
        #     user=factory.Iterator(cycle(users)),
        # )

        # for address in addresses:
        #     address.save()

        # self.stdout.write(
        #     self.style.SUCCESS(
        #         f"Successfully created and saved {len(addresses)} addresses"
        #     )
        # )

        # phones = PhoneFactory.create_batch(
        #     users_count,
        #     user=factory.Iterator(cycle(users)),
        # )

        # for phone in phones:
        #     phone.save()

        # self.stdout.write(
        #     self.style.SUCCESS(
        #         f"Successfully created and saved {len(phones)} phones")
        # )

