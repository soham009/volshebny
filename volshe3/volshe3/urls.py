from django.contrib import admin
from django.urls import include, path

from generateletter import views

urlpatterns = [
    path("", include("generateletter.urls")),
    path("admin/", admin.site.urls),
]
