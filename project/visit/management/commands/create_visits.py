# -*- coding: utf-8 -*-
# myapp/management/commands/create_sample_data.py
from itertools import cycle

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from accounts.factories import *
from visit.factories import *

User = get_user_model()


class Command(BaseCommand):
    help = "Populate the database with sample data"

    def handle(self, *args, **options):
        # Create and save sample data for Category

      
        Patients = Patient.objects.all()
        patients_users= Patient.objects.values_list('user', flat=True)
        print(patients_users)
   
        doctors = Doctor.objects.all()
        doctors_users= Doctor.objects.values_list('user', flat=True)
        visits = VisitFactory.create_batch(
            len(Patient.objects.all()),
            patient=factory.Iterator(cycle(Patients)),
            
            # doctors=factory.Iterator(cycle(doctors)),
        )
            # doctors=[factory.Iterator(cycle(doctors)) for i in range(2)],

        for visit in visits:
            visit.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created and saved {len(visits)} visits"
            )
        )
        # attachments = AttachmentFactory.create_batch(
        #     len(visits),
        #     visit=factory.Iterator(cycle(visits)),
        #     user=factory.Iterator(cycle(patients_users)),
        # )

        # for attachment in attachments:
        #     attachment.save()
        # self.stdout.write(
        #     self.style.SUCCESS(
        #         f"Successfully created and saved {len(attachments)} attachments"
        #     )
        # )
                                          