from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from planes.models import Plane
from planes.api.serializers import PlaneSerializer, AttributeSerializer, ValueSerializer
from planes.repositories.repository import PLaneRepository

from amadeus_api.api.main import Location, amadeus


class PlaneView(viewsets.ViewSet):

    def list(self, request, country_code, city_code):
        pass
    
    def retrieve(self, request, plane_code):
        pass

    