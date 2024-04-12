from django.urls import path, include
from .views import login_page, login

urlpatterns = [
    path("", login_page, name="login_page"),
    path("login/", login, name="login"),
]
