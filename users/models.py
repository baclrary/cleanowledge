from django.contrib.auth.models import AbstractUser
from django.db import models

from . import model_defaults


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=False)
    role = models.CharField(
        choices=model_defaults.UserRole.choices, max_length=100, blank=False, default=model_defaults.UserRole.STUDENT
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f"{self.first_name} {self.middle_name} {self.last_name}"
