from rest_framework.generics import get_object_or_404
from rest_framework.request import Request

from core.factories.amadeus_factory import AmadeusFactory
from tickets.api.serializers import TicketGetSerializer
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
        serializer = TicketGetSerializer(ticket)
        return {
                'code': serializer.data['code'],
                'departure_date': serializer.data['departure_date'],
                'duration': serializer.data['duration'],
                'price': serializer.data['price'],
                }

    def post(self, request: Request) -> dict[str, str]:
        repository = AmadeusFactory.create('amadeus_shopping')
        data = request.data.dict()
        response = repository.cheapest_journey(**data).result['data'][0]
        ticket = generate_ticket_data(response, request)
        serializer = TicketGetSerializer(data=ticket)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return {
                'code': serializer.data['code'],
                'departure_date': serializer.data['departure_date'],
                'duration': serializer.data['duration'],
                'price': serializer.data['price'],
                }

    def update(self, request: Request, ticket_id: int) -> dict[str, str]:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        serializer = TicketGetSerializer(instance=ticket, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return {
                'code': serializer.data['code'],
                'departure_date': serializer.data['departure_date'],
                'duration': serializer.data['duration'],
                'price': serializer.data['price'],
                }

    def delete(self, ticket_id: int) -> dict[str, str]:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        serializer = TicketGetSerializer(ticket)
        serializer.is_valid(raise_exception=True)
        ticket.delete()
        return {
                'code': serializer.data['code'],
                'departure_date': serializer.data['departure_date'],
                'duration': serializer.data['duration'],
                'price': serializer.data['price'],
                }

        