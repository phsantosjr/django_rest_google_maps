import csv
from django.core.management import BaseCommand
from django.utils import timezone
from .models import (
    City, Company, Customer, Occupation, State
)


class Command(BaseCommand):
    help = "Loads products and product categories from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        start_time = timezone.now()
        file_path = options["file_path"]
        with open(file_path, "r") as csv_file:
            data = list(csv.reader(csv_file, delimiter=","))
            for row in data[1:]:
                customer_id = row[0]
                gender = row[4]
                company = Company.objects.get_or_create(name=row[5])
                occupation = Occupation.objects.get_or_create(name=row[7])
                city_state = row[6]
                city_state = city_state.replace('"', '').split(",")
                city = city_state[0]
                state = city_state[1]

                Customer.objects.create(
                    id=customer_id,
                    first_name=row[1],
                    last_name=row[2],
                    email=row[3],
                    gender=gender,
                    company=company,
                    city=city,
                    occupation=occupation
                )
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )