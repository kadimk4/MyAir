from amadeus import Location
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from amadeus_api.api.main import amadeus


class SelfView(APIView):
    def get(self, request):
        response = amadeus.reference_data.locations.get(
            keyword='LON',
            subType=Location.AIRPORT
        )
        return Response(data=response.body, status=status.HTTP_200_OK)
