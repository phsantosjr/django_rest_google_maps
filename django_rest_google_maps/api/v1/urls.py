from django.urls import path
from django.urls import include
from rest_framework import routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

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


schema_view = get_schema_view(
    openapi.Info(
        title="Django Rest + Google Maps",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),
]
