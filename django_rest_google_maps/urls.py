from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("v1/", include("django_rest_google_maps.api.v1.urls", namespace="api-v1")),
]

admin.site.site_header = "Customer Management Address"
admin.site.site_title = "Customer Management"
admin.site.index_title = "Welcome to Customer Management"
