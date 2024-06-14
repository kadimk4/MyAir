from rest_framework.generics import get_object_or_404

from tickets.api.serializers import TicketSerializer
from tickets.models import Ticket
from tickets.repositories.interface import BaseTicket




class TicketRepository(BaseTicket):

    def get_all() -> list[dict]:
        ticket_list = Ticket.objects.all()
        return ticket_list

    def get(ticket_id) -> dict[str, any]:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        serializer = TicketSerializer(ticket)
        return {
            'code': serializer.data['code'],
            'place_code': serializer.data['place_code'],
            'user_id': serializer.data['user_id'],
            'date': serializer.data['date'],
        }

    def post(request) -> dict[str, any]:
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return {
            'code': request.data['code'],
            'place_code': request.data['place_code'],
            'user_id': request.data['user_id'],
            'date': request.data['date'],
        }

    def update(request, ticket_id) -> dict[str, any]:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        serializer = TicketSerializer(instance=ticket, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return {
            'code': serializer.data['code'],
            'place_code': serializer.data['place_code'],
            'user_id': serializer.data['user_id'],
            'date': serializer.data['date'],
        }

    def delete(ticket_id) -> dict[str, any]:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        ticket_data = TicketSerializer(ticket)
        ticket.delete()
        return {
            'code': ticket_data.data['code'],
            'place_code': ticket_data.data['place_code'],
            'user_id': ticket_data.data['user_id'],
            'date': ticket_data.data['date'],
        }

