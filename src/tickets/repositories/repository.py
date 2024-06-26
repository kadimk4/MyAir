from rest_framework.generics import get_object_or_404

from tickets.api.serializers import TicketRequestSerializer
from tickets.models import Ticket
from tickets.repositories.interface import BaseTicket


class TicketRepository(BaseTicket):

    def get_all(self) -> list[dict]:
        ticket_list = Ticket.objects.values(
            'id',
            'code',
            'user_id',
            'date'
        )
        return ticket_list

    def get(self, ticket_id) -> dict[str, any]:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        serializer = TicketRequestSerializer(ticket)
        return {
            'code': serializer.data['code'],
            'place_code': serializer.data['place_code'],
            'user_id': serializer.data['user_id'],
            'date': serializer.data['date'],
        }

    def post(self, request) -> dict[str, any]:
        serializer = TicketRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return {
            'code': request.data['code'],
            'place_code': request.data['place_code'],
            'user_id': request.data['user_id'],
            'date': request.data['date'],
        }

    def update(self, request, ticket_id) -> dict[str, any]:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        serializer = TicketRequestSerializer(instance=ticket, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return {
            'code': serializer.data['code'],
            'place_code': serializer.data['place_code'],
            'user_id': serializer.data['user_id'],
            'date': serializer.data['date'],
        }

    def delete(self, ticket_id) -> dict[str, any]:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        ticket_data = TicketRequestSerializer(ticket)
        ticket.delete()
        return {
            'code': ticket_data.data['code'],
            'place_code': ticket_data.data['place_code'],
            'user_id': ticket_data.data['user_id'],
            'date': ticket_data.data['date'],
        }
