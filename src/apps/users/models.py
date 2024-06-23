from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    passport = models.ImageField(upload_to='passports/', null=True, blank=True)
    link = models.CharField(max_length=10)
