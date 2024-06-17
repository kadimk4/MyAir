from django.db import models
from rest_framework.pagination import PageNumberPagination


class Ticket(models.Model):
    code = models.CharField(max_length=15)
    place_code = models.CharField(max_length=15)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateField()


class BaseTicketPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 25


class LongTicketPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100
