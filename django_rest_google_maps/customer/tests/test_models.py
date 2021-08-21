from django.test import TestCase
import string
from random import choice, randint
from model_bakery import baker
from django_rest_google_maps.customer.models import (
    City, Company, Customer, Occupation, State
)


def get_random_email(length: int) -> str:
    address = get_random_string(length)
    provider = get_random_string(length)
    return f"{address}@{provider}.com"


def get_random_string(length: int) -> str:
    letters = string.ascii_lowercase
    result_str = "".join(choice(letters) for i in range(length))
    return result_str


class OccupationTestCase(TestCase):
    def setUp(self) -> None:
        self.occupation = baker.make("Occupation", name=get_random_string(8))

    def test_object_count(self):
        self.assertGreaterEqual(Occupation.objects.count(), 1)

    def test_attributes_return(self):
        self.assertTrue(hasattr(Occupation, "id"))
        self.assertTrue(hasattr(Occupation, "name"))

    def test_max_length(self):
        length = self.occupation._meta.get_field("name").max_length
        self.assertEqual(length, 100)

    def test_return_str_name(self):
        self.assertEqual(str(self.occupation), f"{self.occupation.name}")


class StateTestCase(TestCase):
    def setUp(self) -> None:
        self.state = baker.make("State", initials=get_random_string(2))

    def test_object_count(self):
        self.assertGreaterEqual(State.objects.count(), 1)

    def test_attributes_return(self):
        self.assertTrue(hasattr(State, "id"))
        self.assertTrue(hasattr(State, "initials"))

    def test_max_length(self):
        length = self.state._meta.get_field("initials").max_length
        self.assertEqual(length, 2)

    def test_return_str_name(self):
        self.assertEqual(str(self.state), f"{self.state.initials}")


class CityTestCase(TestCase):
    def setUp(self) -> None:
        state = baker.make("state", initials=get_random_string(2))
        self.city = baker.make("City", state=state, name=get_random_string(50), _fill_optional=True)

    def test_object_count(self):
        self.assertGreaterEqual(City.objects.count(), 1)

    def test_attributes_return(self):
        self.assertTrue(hasattr(City, "id"))
        self.assertTrue(hasattr(City, "state"))
        self.assertTrue(hasattr(City, "name"))
        self.assertTrue(hasattr(City, "latitude"))
        self.assertTrue(hasattr(City, "longitude"))

    def test_max_length(self):
        length = self.city._meta.get_field("name").max_length
        self.assertEqual(length, 100)

    def test_return_str_name(self):
        self.assertEqual(str(self.city), f"{self.city.name} - {self.city.state}")


class CompanyTestCase(TestCase):
    def setUp(self) -> None:
        self.company = baker.make("Company", name=get_random_string(50))

    def test_object_count(self):
        self.assertGreaterEqual(Company.objects.count(), 1)

    def test_attributes_return(self):
        self.assertTrue(hasattr(Company, "id"))
        self.assertTrue(hasattr(Company, "name"))

    def test_max_length(self):
        length = self.company._meta.get_field("name").max_length
        self.assertEqual(length, 100)

    def test_return_str_name(self):
        self.assertEqual(str(self.company), f"{self.company.name}")


class CustomerTestCase(TestCase):
    def setUp(self) -> None:
        occupation = baker.make("Occupation", name=get_random_string(8))
        state = baker.make("state", initials=get_random_string(2))
        city = baker.make("City", state=state, name=get_random_string(50), _fill_optional=True)

        self.customer = baker.make(
            "Customer",
            first_name=get_random_string(50),
            email=get_random_email(10),
            gender=1,
            occupation=occupation,
            city=city,
            _fill_optional=True,
        )

    def test_object_count(self):
        self.assertGreaterEqual(Customer.objects.count(), 1)

    def test_attributes_return(self):
        self.assertTrue(hasattr(Customer, "id"))
        self.assertTrue(hasattr(Customer, "first_name"))
        self.assertTrue(hasattr(Customer, "last_name"))
        self.assertTrue(hasattr(Customer, "email"))
        self.assertTrue(hasattr(Customer, "gender"))
        self.assertTrue(hasattr(Customer, "company"))
        self.assertTrue(hasattr(Customer, "occupation"))
        self.assertTrue(hasattr(Customer, "city"))

    def test_max_length(self):
        length = self.customer._meta.get_field("first_name").max_length
        self.assertEqual(length, 100)
        length = self.customer._meta.get_field("last_name").max_length
        self.assertEqual(length, 100)

    def test_return_str_name(self):
        self.assertEqual(
            str(self.customer),
            f"{self.customer.id} - {self.customer.first_name} from {self.customer.city}"
        )
