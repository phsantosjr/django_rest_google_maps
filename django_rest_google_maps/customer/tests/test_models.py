from django.test import TestCase
import string
from random import choice, randint
from model_bakery import baker
from django_rest_google_maps.customer.models import (
    City, Company, Customer, Occupation, State
)


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = "".join(choice(letters) for i in range(length))
    return result_str


class OccupationTestCase(TestCase):
    def setUp(self) -> None:
        self.occupation = baker.make("Occupation", nome=get_random_string(8))

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
