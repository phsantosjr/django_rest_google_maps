from rest_framework import serializers

from django_rest_google_maps.customer.models import (
    City,
    Company,
    Customer,
    Genders,
    Occupation,
    State,
)


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ["id", "initials"]


class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = City
        fields = ["id", "name", "state", "latitude", "longitude"]


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = ["id", "name"]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name"]


class CustomerSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    occupation = OccupationSerializer(required=False)
    city = CitySerializer(required=False)
    gender = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "gender",
            "company",
            "occupation",
            "city",
        ]

    def get_gender(self, obj):
        return obj.get_gender_display()

