from django.urls import path, include
from .views import manager_home_page

urlpatterns = [
    path("", manager_home_page, name="manager_home"),
]
