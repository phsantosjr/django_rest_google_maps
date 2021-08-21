import requests
from django.conf import settings

GOOGLE_MAPS_API_KEY = settings.GOOGLE_MAPS_API_KEY


def get_latitude_longitude_google(address: str) -> tuple:
    response = requests.get(
        f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_MAPS_API_KEY}"
    )
    response_dict = response.json()

    if response_dict["status"] == "OK":
        latitude = response_dict["results"][0]["geometry"]["location"]["lat"]
        longitude = response_dict["results"][0]["geometry"]["location"]["lng"]

        return latitude, longitude
    return 0, 0
