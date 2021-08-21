from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from model_bakery import baker


class StateViewSetTestCase(TestCase):
    def test_list_status_code_200(self):
        response = self.client.get(
            reverse("api-v1:state-list")
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CityViewSetTestCase(TestCase):
    ...


class CompanyViewSetTestCase(TestCase):
    ...


class OccupationViewSetTestCase(TestCase):
    ...


class CustomerViewSetTestCase(TestCase):
    ...