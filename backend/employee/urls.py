from django.urls import path, include
from .views import employee_home_page,toggle_clock

urlpatterns = [
    path("", employee_home_page, name="employee_home"),
    path("toggle_clock/<str:username>/",toggle_clock, name="toggle_clock")
]
