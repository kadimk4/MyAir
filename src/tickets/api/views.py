# from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from tickets.api.serializers import TicketSerializer
from tickets.models import TicketPagination
from tickets.repositories.repository import TicketRepository


# Create your views here.
class SelfListView(ListAPIView):
    queryset = TicketRepository.get_all()

    serializer_class = TicketSerializer
    pagination_class = TicketPagination


class SelfView(GenericAPIView):
    serializer_class = TicketSerializer

    def get(self, request, id):
        serializer = TicketRepository.get(request, id)
        return Response(data=serializer, status=status.HTTP_200_OK)


class SelfCreateView(GenericAPIView):
    serializer_class = TicketSerializer

    def post(self, request):
        serializer = TicketRepository.post(request)
        if serializer:
            return Response(data=serializer, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SelfUpdateDeleteView(GenericAPIView):
    serializer_class = TicketSerializer

    def patch(request):
        serializer = TicketRepository.update(request)
        return Response(data=serializer, status=status.HTTP_200_OK)

    def delete(request):
        serializer = TicketRepository.delete(request)
        return Response(data=serializer, status=status.HTTP_200_OK)
