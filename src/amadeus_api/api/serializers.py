from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from amadeus_api.models import FlightOffer

class FlightOfferSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FlightOffer
        fields = '__all__'