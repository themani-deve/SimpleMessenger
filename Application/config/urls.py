from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

APPs_URLs = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("account.presentation.urls")),
]

DOC_URLs = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

urlpatterns = APPs_URLs + DOC_URLs
