from amadeus import Location
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from drf_spectacular.views import extend_schema
from amadeus_api.api.main import amadeus
from amadeus_api.api.serializers import FlightOfferSerializer
from amadeus_api.models import BaseFlightOfferPagination
from amadeus_api.repositories.repository import AirportRepository, ReferenceDataRepository, ShoppingRepository, TravelRepository


@extend_schema(tags=['Amadeus'])
class SelfView(APIView):
    def get(self, request):
        response = amadeus.reference_data.locations.get(
            keyword='LON',
            subType=Location.AIRPORT
        )
        return Response(data=response.body, status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewCheapest_flights(GenericAPIView):
    serializer_class = FlightOfferSerializer
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, city_code):
        repository = ShoppingRepository()
        response = repository.cheapest_flights(city_code)
        return Response(data=response.data[0], status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewFavorable_flights_dates(ListAPIView):
    serializer_class = FlightOfferSerializer
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, city_code_from, city_code_to):
        repository = ShoppingRepository()
        response = repository.favorable_flights_dates(city_code_from=city_code_from, city_code_to=city_code_to)
        return Response(data=response.data, status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewCheapest_journey(GenericAPIView):
    serializer_class = FlightOfferSerializer
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, city_code_from, city_code_to, date, adults_count):
        repository = ShoppingRepository()
        response = repository.cheapest_journey(city_code_from=city_code_from, city_code_to=city_code_to, date=date, adults_count=adults_count)
        print(response)
        return Response(data=response.data[0], status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewPredict_travel_choice(GenericAPIView):
    serializer_class = FlightOfferSerializer
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, city_code_from, city_code_to, date, adults_count):
        repository = ShoppingRepository()
        response = repository.predict_travel_choice(city_code_from=city_code_from, city_code_to=city_code_to, date=date, adults_count=adults_count)
        return Response(data=response.data[0], status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewPredict_travel_purpose(GenericAPIView):
    serializer_class = FlightOfferSerializer
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, city_code_from, city_code_to, departure_date, arrival_date, search_date):
        repository = TravelRepository()
        response = repository.predict_travel_pupose(city_code_from=city_code_from, city_code_to=city_code_to, departure_date=departure_date, arrival_date=arrival_date, search_date=search_date)
        return Response(data=response.data[0], status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewPredict_flight_delay(GenericAPIView):
    serializer_class = FlightOfferSerializer
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, city_code_from, city_code_to, departure_date, arrival_date, arrival_time, aircraft_code, carrier_code, flight_number, duration):
        repository = TravelRepository()
        response = repository.predict_flight_delay(city_code_from=city_code_from, city_code_to=city_code_to, departure_date=departure_date, arrival_date=arrival_date, arrival_time=arrival_time, aircraft_code=aircraft_code, carrier_code=carrier_code, flight_number=flight_number, duration=duration)
        return Response(data=response.data[0], status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewDetails_airport(GenericAPIView):
    serializer_class = FlightOfferSerializer
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, airport_code):
        repository = ReferenceDataRepository()
        response = repository.details_airport(airport_code=airport_code)
        return Response(data=response.data[0], status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewList_near_airports(GenericAPIView):
    serializer_class = FlightOfferSerializer
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, longitude, latitude):
        repository = ReferenceDataRepository()
        response = repository.list_near_airports(longitude=longitude, latitude=latitude)
        return Response(data=response.data[0], status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewCheckin_links(GenericAPIView):
    serializer_class = FlightOfferSerializer
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, airline_code, language):
        repository = ReferenceDataRepository()
        response = repository.checkin_links(airline_code=airline_code, language=language)
        return Response(data=response.data[0], status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewRecommended_locations(GenericAPIView):
    serializer_class = FlightOfferSerializer
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, city_code, country_code):
        repository = ReferenceDataRepository()
        response = repository.recommended_locations(city_code=city_code, country_code=country_code)
        return Response(data=response.data[0], status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewList_city_hotels(GenericAPIView):
    serializer_class = FlightOfferSerializer
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, city_code):
        repository = ReferenceDataRepository()
        response = repository.list_city_hotels(city_code=city_code)
        return Response(data=response.data[0], status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewPercentage_ofontime_departures(GenericAPIView):
    serializer_class = FlightOfferSerializer
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, airport_code, date):
        repository = AirportRepository()
        response = repository.percentage_ofontime_departures(airport_code=airport_code, date=date)
        return Response(data=response.data[0], status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewAirport_direct(GenericAPIView):
    serializer_class = FlightOfferSerializer
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, airport_code):
        repository = AirportRepository()
        response = repository.airport_direct(airport_code=airport_code)
        return Response(data=response.data[0], status=status.HTTP_200_OK)