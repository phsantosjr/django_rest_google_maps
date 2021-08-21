from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from django_rest_google_maps.customer.models import (
    City, Company, Customer, Occupation, State
)

from .serializers import (
    CitySerializer,
    CompanySerializer,
    CustomerSerializer,
    OccupationSerializer,
    StateSerializer,
)

from django_rest_google_maps.customer.models import (
    City,
    Company,
    Customer,
    Occupation,
    State,
)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.filter()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.filter()
    serializer_class = StateSerializer
    filter_backends = [DjangoFilterBackend]


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.filter()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]


class OccupationViewSet(viewsets.ModelViewSet):
    queryset = Occupation.objects.filter()
    serializer_class = OccupationSerializer
    filter_backends = [DjangoFilterBackend]


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.filter()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]

