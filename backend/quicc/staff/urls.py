from django.urls import path, include
from .views import login_page

urlpatterns = [path("", login_page, name="login")]
