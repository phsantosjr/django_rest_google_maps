import json
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

    def test_response_content(self):
        baker.make("State", _fill_optional=True)
        response = self.client.get(
            reverse("api-v1:state-list")
        )

        content = json.loads(response.content)
        self.assertEqual(content["count"], 1)
        self.assertIsNone(content["next"])
        self.assertIsNone(content["previous"])
        self.assertIs(type(content), dict)
        self.assertIs(type(content["results"]), list)

        for item in content["results"]:
            self.assertIn("id", item)
            self.assertIn("initials", item)


class CityViewSetTestCase(TestCase):
    def test_list_status_code_200(self):
        response = self.client.get(
            reverse("api-v1:city-list")
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response_content(self):
        baker.make("City", _fill_optional=True)
        response = self.client.get(
            reverse("api-v1:city-list")
        )

        content = json.loads(response.content)
        self.assertEqual(content["count"], 1)
        self.assertIsNone(content["next"])
        self.assertIsNone(content["previous"])
        self.assertIs(type(content), dict)
        self.assertIs(type(content["results"]), list)

        for item in content["results"]:
            self.assertIn("id", item)
            self.assertIn("name", item)
            self.assertIn("state", item)


class CompanyViewSetTestCase(TestCase):
    def test_list_status_code_200(self):
        response = self.client.get(
            reverse("api-v1:company-list")
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response_content(self):
        baker.make("Company", _fill_optional=True)
        response = self.client.get(
            reverse("api-v1:company-list")
        )

        content = json.loads(response.content)
        self.assertEqual(content["count"], 1)
        self.assertIsNone(content["next"])
        self.assertIsNone(content["previous"])
        self.assertIs(type(content), dict)
        self.assertIs(type(content["results"]), list)

        for item in content["results"]:
            self.assertIn("id", item)
            self.assertIn("name", item)


class OccupationViewSetTestCase(TestCase):
    def test_list_status_code_200(self):
        response = self.client.get(
            reverse("api-v1:occupation-list")
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response_content(self):
        baker.make("Occupation", _fill_optional=True)
        response = self.client.get(
            reverse("api-v1:occupation-list")
        )

        content = json.loads(response.content)
        self.assertEqual(content["count"], 1)
        self.assertIsNone(content["next"])
        self.assertIsNone(content["previous"])
        self.assertIs(type(content), dict)
        self.assertIs(type(content["results"]), list)

        for item in content["results"]:
            self.assertIn("id", item)
            self.assertIn("name", item)


class CustomerViewSetTestCase(TestCase):
    def test_list_status_code_200(self):
        response = self.client.get(
            reverse("api-v1:customer-list")
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response_content(self):
        baker.make("Customer", _fill_optional=True)
        response = self.client.get(
            reverse("api-v1:customer-list")
        )

        content = json.loads(response.content)
        self.assertEqual(content["count"], 1)
        self.assertIsNone(content["next"])
        self.assertIsNone(content["previous"])
        self.assertIs(type(content), dict)
        self.assertIs(type(content["results"]), list)

        for item in content["results"]:
            self.assertIn("id", item)
            self.assertIn("first_name", item)
            self.assertIn("last_name", item)
            self.assertIn("email", item)
            self.assertIn("gender", item)
            self.assertIn("company", item)
            self.assertIn("occupation", item)
            self.assertIn("city", item)

