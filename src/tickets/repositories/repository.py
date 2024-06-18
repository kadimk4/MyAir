from rest_framework.generics import get_object_or_404
from rest_framework.request import Request

from core.factories.amadeus_factory import AmadeusFactory
from tickets.api.serializers import TicketSerializer
from tickets.models import Ticket
from tickets.repositories.interface import BaseTicket
from tickets.services.generator import generate_ticket_data



class TicketRepository(BaseTicket):

    def get_all(self) -> list[dict]:
        ticket_list = Ticket.objects.values(
            'id',
            'code',
            'departure_date',
            'duration',
            'price',
            'user_id'
        )
        return ticket_list

    def get(self, ticket_id: int) -> dict[str, str]:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        serializer = TicketSerializer(ticket)
        return {
            'code': serializer.data['code'],
            'departure_date': serializer.data['departure_date'],
            'duration': serializer.data['duration'],
            'price': serializer.data['price'],
            'user_id': serializer.data['user_id']
        }

    def post(self, request: Request) -> dict[str, str]:
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return {
            'code': serializer.data['code'],
            'departure_date': serializer.data['departure_date'],
            'duration': serializer.data['duration'],
            'price': serializer.data['price'],
            'user_id': serializer.data['user_id']
        }

    def update(self, request: Request, ticket_id: int) -> dict[str, str]:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        serializer = TicketSerializer(instance=ticket, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return {
            'code': serializer.data['code'],
            'departure_date': serializer.data['departure_date'],
            'duration': serializer.data['duration'],
            'price': serializer.data['price'],
            'user_id': serializer.data['user_id']
        }

    def delete(self, ticket_id: int) -> dict[str, str]:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        ticket_data = TicketSerializer(ticket)
        ticket.delete()
        return {
            'code': ticket_data.data['code'],
            'departure_date': ticket_data.data['departure_date'],
            'duration': ticket_data.data['duration'],
            'price': ticket_data.data['price'],
            'user_id': ticket_data.data['user_id']
        }

    def get_ticket(self, request: Request) -> dict[str, str]:
        repository = AmadeusFactory.create('amadeus_shopping')
        data = request.data.dict()
        response = repository.cheapest_journey(**data).result['data'][0]
        ticket = generate_ticket_data(response)
        ticket['user_id'] = request.user.id
        ticket['departure_date'] = data['date']
        ticket_data = TicketSerializer(data=ticket)
        ticket_data.is_valid(raise_exception=True)
        ticket_data.save()
        return {
            'code': ticket_data.data['code'],
            'departure_date': ticket_data.data['departure_date'],
            'duration': ticket_data.data['duration'],
            'price': ticket_data.data['price'],
            'user_id': ticket_data.data['user_id'],
        }
        