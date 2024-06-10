from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.pagination import PageNumberPagination

class UserPaginator(PageNumberPagination):
    page_size = 20

class User(AbstractUser):
    passport = models.ImageField(upload_to="passports/", null=True, blank=True)
    link = models.CharField(max_length=10)
    

