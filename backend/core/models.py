from django.db import models
from login.models import User


# Create your models here.
class Shift(models.Model):

    employee = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(to="Org", on_delete=models.SET_NULL, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    reg_hr = models.IntegerField()
    night_diff = models.IntegerField()
    night_diff = night_diff
    overtime = models.IntegerField()
    total_hours = models.IntegerField()

    def __str__(self) -> str:
        return (
            str(self.employee)
            + " "
            + str(self.start)
            + "-"
            + str(self.end)
            + " at "
            + str(self.organization)
        )


class Org(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.name
