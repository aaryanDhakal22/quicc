from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, role, password=None, **extra_fields):
        user = self.model(username=username.strip(), role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, role, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, role, password, **extra_fields)


class User(AbstractBaseUser):
    identifier = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=16)

    EMPLOYEE = "E"
    MANAGER = "M"
    ROLE_CHOICES = [
        (EMPLOYEE, "Employee"),
        (MANAGER, "Manager"),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=EMPLOYEE)

    REQUIRED_FIELDS = ["role"]
    USERNAME_FIELD = "identifier"

    objects = UserManager()

    def __str__(self):
        return self.username

    def status(self):
        return self.role
