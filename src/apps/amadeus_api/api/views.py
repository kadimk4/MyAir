from drf_spectacular.views import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from utils.factories.amadeus_factory import AmadeusFactory


@extend_schema(tags=['Shopping'])
class CheapestFlightsView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_shopping')
        response = repository.cheapest_flights(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Shopping'])
class FavorableFlightsDatesView(ListAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_shopping')
        response = repository.favorable_flights_dates(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Shopping'])
class CheapestJourneyView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_shopping')
        response = repository.cheapest_journey(**parameters)
        return Response(data=response.data, status=status.HTTP_200_OK)


@extend_schema(tags=['Shopping'])
class PredictTravelChoiceView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_shopping')
        response = repository.predict_travel_choice(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Travel'])
class PredictTravelPurposeView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_travel')
        response = repository.predict_travel_purpose(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Travel'])
class PredictFlightDelayView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_travel')
        response = repository.predict_flight_delay(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Reference'])
class DetailsAirportView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_reference')
        response = repository.details_airport(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Reference'])
class ListNearAirportsView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_reference')
        response = repository.list_near_airports(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Reference'])
class CheckinLinksView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_reference')
        response = repository.checkin_links(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Reference'])
class RecommendedLocationsView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_reference')
        response = repository.recommended_locations(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Reference'])
class ListCityHotelsView(GenericAPIView):

    def get(self, request: Request, **parameters: str) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_reference')
        response = repository.list_city_hotels(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Airport'])
class PercentageOnTimeDeparturesView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_airport')
        response = repository.percentage_ofontime_departures(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Airport'])
class AirportDirectView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        repository = AmadeusFactory.create('amadeus_airport')
        response = repository.airport_direct(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)
