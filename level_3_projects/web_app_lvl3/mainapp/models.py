from django.db import models
from django.db.models import EmailField


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=32, unique=True)
    user_email = models.EmailField(default='default@example.com')
    user_password = models.CharField(max_length=128)

    def __str__(self):
        return self.user_name
