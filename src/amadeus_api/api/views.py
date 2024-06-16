from amadeus import Location
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from drf_spectacular.views import extend_schema
from amadeus_api.api.main import amadeus

from amadeus_api.models import BaseFlightOfferPagination

from core.factories.rep_factory import RepositoryFactory


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
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, **parameters):
        repository = RepositoryFactory.create('amadeus_shopping')
        response = repository.cheapest_flights(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewFavorable_flights_dates(ListAPIView):
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, **parameters):
        repository = RepositoryFactory.create('amadeus_shopping')
        response = repository.favorable_flights_dates(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewCheapest_journey(GenericAPIView):
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, **parameters):
        repository = RepositoryFactory.create('amadeus_shopping')
        response = repository.cheapest_journey(**parameters)
        return Response(data=response.data, status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewPredict_travel_choice(GenericAPIView):
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, **parameters):
        repository = RepositoryFactory.create('amadeus_shopping')
        response = repository.predict_travel_choice(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewPredict_travel_purpose(GenericAPIView):
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, **parameters):
        repository = RepositoryFactory.create('amadeus_travel')
        response = repository.predict_travel_purpose(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewPredict_flight_delay(GenericAPIView):
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, **parameters):
        repository = RepositoryFactory.create('amadeus_travel')
        response = repository.predict_flight_delay(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewDetails_airport(GenericAPIView):
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, **parameters):
        repository = RepositoryFactory.create('amadeus_reference')
        response = repository.details_airport(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewList_near_airports(GenericAPIView):
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, **parameters):
        repository = RepositoryFactory.create('amadeus_reference')
        response = repository.list_near_airports(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewCheckin_links(GenericAPIView):
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, **parameters):
        repository = RepositoryFactory.create('amadeus_reference')
        response = repository.checkin_links(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewRecommended_locations(GenericAPIView):
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, **parameters):
        repository = RepositoryFactory.create('amadeus_reference')
        response = repository.recommended_locations(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewList_city_hotels(GenericAPIView):
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, **parameters):
        repository = RepositoryFactory.create('amadeus_reference')
        response = repository.list_city_hotels(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewPercentage_ofontime_departures(GenericAPIView):
    pagination_class = BaseFlightOfferPagination
    
    def get(self, request, **parameters):
        repository = RepositoryFactory.create('amadeus_airport')
        response = repository.percentage_ofontime_departures(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)

@extend_schema(tags=['Amadeus'])
class SelfViewAirport_direct(GenericAPIView):
    pagination_class = BaseFlightOfferPagination
    
    def get(self,request, **parameters):
        repository = RepositoryFactory.create('amadeus_airport')
        response = repository.airport_direct(**parameters)
        print(response)
        return Response(data=response, status=status.HTTP_200_OK)