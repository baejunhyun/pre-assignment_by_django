from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "status_parsing"

urlpatterns = [
    path("", views.package_list_view, name="package_list_view"),
    path("<int:pk>/", views.package_detail_view, name="package_detail_view"),
    path("parse/", views.package_parsing_view, name="package_parsing_view"),
]
