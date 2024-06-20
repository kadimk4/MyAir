from django.db.models import Model
from rest_framework import serializers

from tickets.models import Ticket
from users.models import User


class TicketGetSerializer(serializers.ModelSerializer):

    class Meta:
        model: Model = Ticket
        fields: list[str] = [
            'id',
            'code',
            'departure_date',
            'duration',
            'price',
            'user_id'
        ]


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model: Model = Ticket
        fields: list[str] = [
            'code',
            'departure_date',
            'duration',
            'price',
        ]
