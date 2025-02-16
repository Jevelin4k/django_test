from django.db import models
from django.db.models import Model


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name