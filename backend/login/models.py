from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, role, password=None):
        user = self.model(username=username.strip(), role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, role, password):
        user = self.create_user(
            username=username,
            role=role,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_clocked_in = models.BooleanField(default=False)
    
    EMPLOYEE = "E"
    MANAGER = "M"
    ROLE_CHOICES = [
        (EMPLOYEE, "Employee"),
        (MANAGER, "Manager"),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=EMPLOYEE)

    REQUIRED_FIELDS = ["role"]
    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return self.username

    def status(self):
        return self.role

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
