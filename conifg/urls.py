from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("ibrat/_admin/", admin.site.urls),
    path("ibrat/", include("core.urls", namespace="core"))
]
