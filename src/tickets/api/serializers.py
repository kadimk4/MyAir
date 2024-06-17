from django.db.models import Model
from rest_framework import serializers

from tickets.models import Ticket


class TicketRequestSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    class Meta:
        model: Model = Ticket
        fields: list[str] = [
            'id',
            'code',
            'place_code',
            'user_id',
            'date'
        ]


class TicketResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model: Model = Ticket
        fields: list[str] = [
            'code',
            'place_code',
            'user_id',
            'date'
        ]
