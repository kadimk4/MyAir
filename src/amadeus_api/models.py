from django.db import models
from rest_framework.pagination import PageNumberPagination


class FlightOffer(models.Model):
    type = models.CharField(max_length=20)
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)
    departureDate = models.DateField()
    returnDate = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    flightDates_link = models.URLField()  
    flightOffers_link = models.URLField()


class BaseFlightOfferPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 25

class LongFlightOfferPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100