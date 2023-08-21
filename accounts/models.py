from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name: models.CharField = models.CharField(null=True, blank=True, max_length=255)
