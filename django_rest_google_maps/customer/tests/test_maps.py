from django.test import SimpleTestCase, override_settings
from vcr import VCR

from ..maps import get_latitude_longitude_google

vcr = VCR(
    cassette_library_dir="django_rest_google_maps/customer/tests/resources/cassettes",
    path_transformer=VCR.ensure_suffix(".yml"),
    filter_headers=["authorizations"],
    record_mode="none",
    match_on=["method", "path", "query"],
)


@override_settings(GOOGLE_MAPS_API_KEY="google_key")
class GoogleMapsGeoCodingTestCase(SimpleTestCase):
    @vcr.use_cassette("django_rest_google_maps/customer/tests/resources/cassettes/geo-code-success.yml")
    def test_return_geo_coding_success(self):
        address = "Av Paulista, 2000, São Paulo, SP"
        lat, long = get_latitude_longitude_google(address)
        self.assertEqual(lat, -23.5588414)
        self.assertEqual(long, -46.6588714)
