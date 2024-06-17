from django.db import models


class Ticket(models.Model):
    code = models.CharField(max_length=15)
    place_code = models.CharField(max_length=15)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateField()
