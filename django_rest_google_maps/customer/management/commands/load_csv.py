import os
import csv
from django.core.management import BaseCommand
from django.conf import settings

from django_rest_google_maps.customer.models import (
    City, Company, Customer, Occupation, State, Genders
)
from django_rest_google_maps.customer.maps import get_latitude_longitude_google

FOLDER_IMPORT = 'contrib'


class Command(BaseCommand):
    help = "Loads customers and related data from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("file", type=str)

    def handle(self, *args, **options):
        file = options["file"]
        file_path = settings.BASE_DIR / FOLDER_IMPORT / file

        try:
            with open(file_path, "r") as csv_file:
                data = list(csv.reader(csv_file, delimiter=","))

                for row in data[1:]:
                    os.system('clear')
                    print("Now we are loading this data below:")
                    print(row)

                    customer_id = row[0]
                    gender = self._get_gender_id(row[4])
                    if row[5]:
                        company = Company.objects.get_or_create(name=row[5])
                    if row[7]:
                        occupation = Occupation.objects.get_or_create(name=row[7])
                    city_state = row[6]
                    if city_state:
                        city_state = city_state.replace('"', '').split(",")
                        city = city_state[0]
                        state = State.objects.get_or_create(initials=city_state[1])
                        latitude, longitude = self._get_latitude_longitude(city_state[0], city_state[1])
                        city = City.objects.get_or_create(
                            name=city,
                            state_id=state[0].id,
                            latitude=latitude,
                            longitude=longitude
                        )

                    Customer.objects.update_or_create(
                        id=customer_id,
                        first_name=row[1],
                        last_name=row[2],
                        email=row[3],
                        gender=gender,
                        company=company[0] or None,
                        city=city[0] or None,
                        occupation=occupation[0] or None
                    )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Loading CSV was finished !"
                )
            )

        except FileNotFoundError as ex:
            raise Exception("File not found, be sure that the file is in correct path !")

    @staticmethod
    def _get_gender_id(gender: str) -> int:
        try:
            if not gender:
                return 3
            return [x.value for x in Genders if x.label == gender][0]
        except IndexError:
            return 3

    @staticmethod
    def _get_latitude_longitude(city: str, state: str) -> tuple:
        return get_latitude_longitude_google(f"{city}, {state}")
