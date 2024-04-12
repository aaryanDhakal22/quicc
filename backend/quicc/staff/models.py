from django.db import models


# Create your models here.
class Staff(models.Model):
    text = models.CharField(max_length=10)
