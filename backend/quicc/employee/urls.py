from django.urls import path, include
from .views import employee_home_page

urlpatterns = [
    path("", employee_home_page, name="employee_home"),
]
