from rest_framework.generics import get_object_or_404
from rest_framework.request import Request

from core.factories.amadeus_factory import AmadeusFactory
from tickets.api.serializers import TicketRequestSerializer, TicketResponseSerializer
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
        serializer = TicketRequestSerializer(ticket)
        return serializer.data

    def post(self, request: Request) -> dict[str, str]:
        serializer = TicketRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    def update(self, request: Request, ticket_id: int) -> dict[str, str]:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        serializer = TicketRequestSerializer(instance=ticket, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    def delete(self, ticket_id: int) -> dict[str, str]:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        serializer = TicketRequestSerializer(ticket)
        serializer.is_valid(raise_exception=True)
        ticket.delete()
        return serializer.data

    def get_ticket(self, request: Request) -> dict[str, str]:
        repository = AmadeusFactory.create('amadeus_shopping')
        data = request.data.dict()
        response = repository.cheapest_journey(**data).result['data'][0]
        ticket = generate_ticket_data(response)
        ticket['user_id'] = request.user.id
        ticket['departure_date'] = data['date']
        serializer = TicketRequestSerializer(data=ticket)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data
        