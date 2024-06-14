from rest_framework import serializers

from tickets.models import Ticket


class TicketRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'code',
            'place_code',
            'user_id',
            'date'
        ]

class TicketResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'code',
            'place_code',
            'user_id',
            'date'
        ]