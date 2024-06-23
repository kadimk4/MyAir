from django.db.models import Model
from rest_framework import serializers

from apps.tickets.models import Ticket


class TicketGetSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

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
