from rest_framework.generics import get_object_or_404

from tickets.api.serializers import TicketSerializer
from tickets.models import Ticket
from tickets.services.user import is_valid_ticket
from users.repositories.interface import BaseTicket


class TicketRepository(BaseTicket):

    def get_all() -> list[dict]:
        ticket_list = Ticket.objects.all()
        return ticket_list

    def get(request, id) -> dict[str, any]:
        ticket = get_object_or_404(Ticket, pk=id)
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

    def update(request) -> dict[str, any]:
        ticket_id = request.data['id']
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        serializer = TicketSerializer(instance=ticket, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return {
            'code': request.data['code'],
            'place_code': request.data['place_code'],
            'user_id': request.data['user_id'],
            'date': request.data['date'],
                }

    def delete(request) -> dict[str, any]:
        ticket_id = request.data['id']
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        ticket.delete()

        return {
            'code': request.data['code'],
            'place_code': request.data['place_code'],
            'user_id': request.data['user_id'],
            'date': request.data['date'],
                }