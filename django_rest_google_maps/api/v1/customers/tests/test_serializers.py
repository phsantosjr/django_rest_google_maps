from django.test import TestCase
from model_bakery import baker

from ..serializers import (
    CitySerializer,
    CompanySerializer,
    CustomerSerializer,
    OccupationSerializer,
    StateSerializer,
)
from django_rest_google_maps.customer.tests.test_base import (
    get_random_email,
    get_random_string,
)
from django_rest_google_maps.customer.models import Genders


class StateSerializerTest(TestCase):
    def setUp(self) -> None:
        self.state = baker.make("State", initials=get_random_string(2))
        self.serializer = StateSerializer(instance=self.state)

    def test_serializer(self):
        self.assertEqual(self.serializer.data.keys(), {"id", "initials"})

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["id"], self.state.id)
        self.assertEqual(data["initials"], self.state.initials)


class CitySerializerTest(TestCase):
    def setUp(self) -> None:
        state = baker.make("State", initials=get_random_string(2))
        self.city = baker.make("City", name=get_random_string(20), state=state)
        self.serializer = CitySerializer(instance=self.city)

    def test_serializer(self):
        self.assertEqual(self.serializer.data.keys(), {"id", "name", "state", "latitude", "longitude"})

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["id"], self.city.id)
        self.assertEqual(data["name"], self.city.name)
        self.assertEqual(data["latitude"], self.city.latitude)
        self.assertEqual(data["longitude"], self.city.longitude)


class OccupationSerializerTest(TestCase):
    def setUp(self) -> None:
        self.occupation = baker.make("Occupation", name=get_random_string(20))
        self.serializer = OccupationSerializer(instance=self.occupation)

    def test_serializer(self):
        self.assertEqual(self.serializer.data.keys(), {"id", "name"})

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["id"], self.occupation.id)
        self.assertEqual(data["name"], self.occupation.name)


class CompanySerializerTest(TestCase):
    def setUp(self) -> None:
        self.company = baker.make("Company", name=get_random_string(20))
        self.serializer = CompanySerializer(instance=self.company)

    def test_serializer(self):
        self.assertEqual(self.serializer.data.keys(), {"id", "name"})

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["id"], self.company.id)
        self.assertEqual(data["name"], self.company.name)


class CustomerSerializerTest(TestCase):
    def setUp(self) -> None:
        occupation = baker.make("Occupation", name=get_random_string(8))
        state = baker.make("state", initials=get_random_string(2))
        city = baker.make(
            "City", state=state, name=get_random_string(50), _fill_optional=True
        )
        self.customer = baker.make(
            "Customer",
            first_name=get_random_string(50),
            email=get_random_email(10),
            gender=Genders.FEMALE,
            occupation=occupation,
            city=city,
            _fill_optional=True,
        )
        self.serializer = CustomerSerializer(instance=self.customer)

    def test_serializer(self):
        self.assertEqual(
            self.serializer.data.keys(),
            {
                "id",
                "first_name",
                "last_name",
                "email",
                "gender",
                "company",
                "occupation",
                "city",
            },
        )

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["id"], self.customer.id)
        self.assertEqual(data["first_name"], self.customer.first_name)
        self.assertEqual(data["last_name"], self.customer.last_name)
        self.assertEqual(data["email"], self.customer.email)
        self.assertEqual(data["gender"], Genders.FEMALE.label)
        self.assertEqual(data["company"]["name"], self.customer.company.name)
        self.assertEqual(data["occupation"]["name"], self.customer.occupation.name)
        self.assertEqual(data["city"]["name"], self.customer.city.name)
