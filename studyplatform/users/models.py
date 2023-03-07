from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=False)
    role = models.CharField(max_length=100, blank=False, default='student')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
