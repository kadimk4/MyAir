from django.db import models


class Ticket(models.Model):
    # CLASS AIR_COMPANY IATA_FROM AIR_COMPANY_CODE IATA_TO
    code = models.CharField(max_length=15)
    # YYYY-MM-DD
    departure_date = models.DateField()
    # HH:MM:SS
    duration = models.CharField()
    price = models.CharField()
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
