from rest_framework.generics import get_object_or_404
from rest_framework.request import Request

from apps.tickets.api.serializers import TicketGetSerializer
from apps.tickets.models import Ticket
from apps.tickets.repositories.interface import BaseTicket
from apps.tickets.services.generator import generate_ticket_data
from utils.factories.service_factory import ServiceFactory


class TicketRepository(BaseTicket):

    def get_all(self) -> list[dict]:
        ticket_list = Ticket.objects.all().order_by('id')
        return ticket_list

    def get_self_tickets(self, request) -> list[dict]:
        ticket_list = Ticket.objects.filter(user_id=request.user.id).values(
            'code',
            'departure_date',
            'duration',
            'price',
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
        repository = ServiceFactory.create('amadeus_shopping')
        data = request.data
        response = repository.cheapest_journey(
            city_code_from=data['city_code_from'], city_code_to=data['city_code_to'], date=data['date'], adults_count=data['adults_count']).result['data'][0]
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
        ticket.delete()
        return {
            'code': serializer.data['code'],
            'departure_date': serializer.data['departure_date'],
            'duration': serializer.data['duration'],
            'price': serializer.data['price'],
        }
