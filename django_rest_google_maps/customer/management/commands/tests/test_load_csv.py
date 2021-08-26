from django.test import SimpleTestCase, override_settings
from vcr import VCR

from ..load_csv import FOLDER_IMPORT, Command
from django_rest_google_maps.customer.models import GENDERS


vcr = VCR(
    cassette_library_dir="django_rest_google_maps/customer/tests/resources/cassettes",
    path_transformer=VCR.ensure_suffix(".yml"),
    filter_headers=["authorizations"],
    record_mode="none",
    match_on=["method", "path", "query"],
)


class FolderImportTestCase(SimpleTestCase):
    def test_value_ok(self):
        self.assertEqual(FOLDER_IMPORT, 'contrib')


@override_settings(GOOGLE_MAPS_API_KEY="google_key")
class CommandTestCase(SimpleTestCase):
    def test_help(self):
        self.assertEqual(Command.help, "Loads customers and related data from CSV file.")

    def test_get_gender_id_female(self):
        self.assertEqual(Command._get_gender_id("Female"), 1)

    def test_get_gender_id_male(self):
        self.assertEqual(Command._get_gender_id("Male"), 2)

    def test_get_gender_id_na(self):
        self.assertEqual(Command._get_gender_id(""), 3)

    @vcr.use_cassette("django_rest_google_maps/customer/tests/resources/cassettes/geo-code-success.yml")
    def test_return_get_latitude_longitude(self):
        city = "Santos"
        state = "SP"
        lat, long = Command._get_latitude_longitude(city, state)
        self.assertEqual(lat, -23.9592201)
        self.assertEqual(long, -46.3317787)

