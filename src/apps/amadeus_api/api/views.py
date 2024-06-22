from drf_spectacular.views import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from utils.factories.service_factory import ServiceFactory


@extend_schema(tags=['Shopping'])
class CheapestFlightsView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        service = ServiceFactory.create('amadeus_shopping')
        response = service.cheapest_flights(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Shopping'])
class FavorableFlightsDatesView(ListAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        service = ServiceFactory.create('amadeus_shopping')
        response = service.favorable_flights_dates(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Shopping'])
class CheapestJourneyView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        service = ServiceFactory.create('amadeus_shopping')
        response = service.cheapest_journey(**parameters)
        return Response(data=response.data, status=status.HTTP_200_OK)


@extend_schema(tags=['Shopping'])
class PredictTravelChoiceView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        service = ServiceFactory.create('amadeus_shopping')
        response = service.predict_travel_choice(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Travel'])
class PredictTravelPurposeView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        service = ServiceFactory.create('amadeus_travel')
        response = service.predict_travel_purpose(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Travel'])
class PredictFlightDelayView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        service = ServiceFactory.create('amadeus_travel')
        response = service.predict_flight_delay(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Reference'])
class DetailsAirportView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        service = ServiceFactory.create('amadeus_reference')
        response = service.details_airport(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Reference'])
class ListNearAirportsView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        service = ServiceFactory.create('amadeus_reference')
        response = service.list_near_airports(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Reference'])
class CheckinLinksView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        service = ServiceFactory.create('amadeus_reference')
        response = service.checkin_links(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Reference'])
class RecommendedLocationsView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        service = ServiceFactory.create('amadeus_reference')
        response = service.recommended_locations(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Reference'])
class ListCityHotelsView(GenericAPIView):

    def get(self, request: Request, **parameters: str) -> Response[list[dict[str, str]]]:
        service = ServiceFactory.create('amadeus_reference')
        response = service.list_city_hotels(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Airport'])
class PercentageOnTimeDeparturesView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        service = ServiceFactory.create('amadeus_airport')
        response = service.percentage_ofontime_departures(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)


@extend_schema(tags=['Airport'])
class AirportDirectView(GenericAPIView):

    def get(self, request: Request, **parameters: dict[str, str]) -> Response[list[dict[str, str]]]:
        service = ServiceFactory.create('amadeus_airport')
        response = service.airport_direct(**parameters)
        return Response(data=response, status=status.HTTP_200_OK)
