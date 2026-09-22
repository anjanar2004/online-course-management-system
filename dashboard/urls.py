from django.urls import path

from . import views
from .reports import reports_view

urlpatterns = [

    path("", views.dashboard_view, name="dashboard"),

    path("reports/", reports_view, name="reports"),

]