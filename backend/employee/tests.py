from django.test import TestCase
from login.models import User


# Create your tests here.
# Test if the user with 'aaryan' and password 'aaryan' can login
class LoginTest(TestCase):
    def test_can_login(self):
        new_user = User.objects.create_user(
            username="aaryan", password="aaryan", role="E"
        )
        new_user.save()

        response = self.client.post("/", {"username": "aaryan", "password": "aaryan"})
        self.assertRedirects(response, "/employee/")
        response = self.client.get("/employee/")
        self.assertContains(response, "aaryan")
        self.assertContains(response, "Employee")
        self.assertContains(response, "Clock In")

    def test_cannot_login_with_wrong_credentials(self):
        new_user = User.objects.create_user(
            username="aaryan", password="aaryan", role="E"
        )
        new_user.save()

        response = self.client.post("/", {"username": "aaryan", "password": "wrong"})
        self.assertContains(response, "Invalid login")

    def test_can_logout(self):
        new_user = User.objects.create_user(
            username="aaryan", password="aaryan", role="E"
        )
        new_user.save()

        self.client.post("/", {"username": "aaryan", "password": "aaryan"})
        response = self.client.get("/employee/")
        self.assertContains(response, "aaryan")
        self.client.get("/logout/")
        response = self.client.get("/employee/")
        self.assertRedirects(response, "/")
