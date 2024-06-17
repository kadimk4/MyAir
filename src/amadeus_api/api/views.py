from drf_spectacular.views import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from core.factories.amadeus_factory import AmadeusFactory


@extend_schema(tags=['Amadeus'])
class CheapestFlightsView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_shopping')
        response = repository.cheapest_flights(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Amadeus'])
class FavorableFlightsDatesView(ListAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_shopping')
        response = repository.favorable_flights_dates(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Amadeus'])
class CheapestJourneyView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_shopping')
        response = repository.cheapest_journey(**parameters)
        return Response(data=response.data, status=status.HTTP_200_OK)


@extend_schema(tags=['Amadeus'])
class PredictTravelChoiceView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_shopping')
        response = repository.predict_travel_choice(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Amadeus'])
class PredictTravelPurposeView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_travel')
        response = repository.predict_travel_purpose(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Amadeus'])
class PredictFlightDelayView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_travel')
        response = repository.predict_flight_delay(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Amadeus'])
class DetailsAirportView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_reference')
        response = repository.details_airport(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Amadeus'])
class ListNearAirportsView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_reference')
        response = repository.list_near_airports(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Amadeus'])
class CheckinLinksView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_reference')
        response = repository.checkin_links(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Amadeus'])
class RecommendedLocationsView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_reference')
        response = repository.recommended_locations(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Amadeus'])
class ListCityHotelsView(GenericAPIView):

    def get(self, request: Request, **parameters: str) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_reference')
        response = repository.list_city_hotels(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Amadeus'])
class PercentageOnTimeDeparturesView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_airport')
        response = repository.percentage_ofontime_departures(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Amadeus'])
class AirportDirectView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_airport')
        response = repository.airport_direct(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)
