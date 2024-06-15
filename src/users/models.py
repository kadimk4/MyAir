from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.pagination import PageNumberPagination




class User(AbstractUser):
    passport = models.ImageField(upload_to='passports/', null=True, blank=True)
    link = models.CharField(max_length=10)

class BaseUserPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 10

class LongUserPagination(PageNumberPagination):
    page_size = 50
    page_query_param = 'page_size'
    max_page_size = 50