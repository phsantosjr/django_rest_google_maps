from django.urls import path
from django.urls import include
from rest_framework import routers

from .customers.views import (
    CityViewSet,
    CompanyViewSet,
    CustomerViewSet,
    OccupationViewSet,
    StateViewSet,
)

app_name = "api.v1"

router = routers.SimpleRouter()
router.register("city", CityViewSet, basename="city")
router.register("company", CompanyViewSet, basename="company")
router.register("customer", CustomerViewSet, basename="customer")
router.register("occupation", OccupationViewSet, basename="occupation")
router.register("state", StateViewSet, basename="state")


urlpatterns = [
    path("", include(router.urls)),
]
