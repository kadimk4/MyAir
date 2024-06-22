from amadeus import Hotel
from amadeus.client.response import Response

from apps.amadeus_api.api.main import amadeus


class ShoppingService:

    def __init__(self) -> None:
        self.request = amadeus.shopping

    def cheapest_flights(self, city_code: str) -> dict[str, str]:
        request = self.request.flight_destinations.get(origin=city_code)
        return request.data

    def favorable_flights_dates(self, city_code_from: str, city_code_to: str) -> dict[str, str]:
        request = self.request.flight_dates.get(origin=city_code_from, destination=city_code_to)
        return request.data

    def cheapest_journey(self, city_code_from: str, city_code_to: str, date: str, adults_count: str) -> Response:
        request = self.request.flight_offers_search.get(
            originLocationCode=city_code_from,
            destinationLocationCode=city_code_to,
            departureDate=date,
            adults=adults_count
        )
        return request

    def predict_travel_choice(self, city_code_from: str, city_code_to: str, date: str, adults_count: str) -> dict[str, str]:
        request = self.request.flight_offers.prediction.post(
            self.cheapest_journey(city_code_from, city_code_to, date, adults_count).result)
        return request.data


class TravelService:

    def __init__(self) -> None:
        self.request = amadeus.travel

    def predict_travel_purpose(self, city_code_from: str, city_code_to: str, departure_date: str, arrival_date: str, search_date: str) -> dict[str, str]:
        request = self.request.predictions.trip_purpose.get(
            originLocationCode=city_code_from,
            destinationLocationCode=city_code_to,
            departureDate=departure_date,
            returnDate=arrival_date,
            searchDate=search_date
        )

        return request.data

    def predict_flight_delay(self, city_code_from: str, city_code_to: str, departure_date: str, departure_time: str, arrival_date: str, arrival_time: str, aircraft_code: str, carrier_code: str, flight_number: str, duration: str) -> dict[str, str]:
        request = self.request.predictions.flight_delay.get(
            originLocationCode=city_code_from,
            destinationLocationCode=city_code_to,
            departureDate=departure_date,
            departureTime=departure_time,
            arrivalDate=arrival_date,
            arrivalTime=arrival_time,
            aircraftCode=aircraft_code,
            carrierCode=carrier_code,
            flightNumber=flight_number,
            duration=duration
        )
        return request.data


class ReferenceDataService:

    def __init__(self) -> None:
        self.request = amadeus.reference_data

    def details_airport(self, airport_code: str) -> dict[str, str]:
        request = self.request.location(airport_code).get()
        return request.data

    def list_near_airports(self, longitude: float, latitude: float) -> dict[str, str]:
        request = self.request.locations.airports.get(longitude=longitude, latitude=latitude)
        return request.data

    def checkin_links(self, airline_code: str, language: str = 'en-GB') -> dict[str, str]:
        request = self.request.urls.checkin_links.get(airlineCode=airline_code, language=language)
        return request.data

    def recommended_locations(self, city_code: str, country_code: str) -> dict[str, str]:
        request = self.request.recommended_locations.get(cityCodes=city_code, travelerCountryCode=country_code)
        return request.data

    def list_city_hotels(self, city_code: str) -> dict[str, str]:
        request = self.request.locations.hotel.get(keyword=city_code, subType=[Hotel.HOTEL_LEISURE, Hotel.HOTEL_GDS])
        return request.data


class AirportService:

    def __init__(self) -> None:
        self.request = amadeus.airport

    def percentage_ofontime_departures(self, airport_code: str, date: str) -> dict[str, str]:
        request = self.request.predictions.on_time.get(airportCode=airport_code, date=date)
        return request.data

    def airport_direct(self, airport_code: str) -> dict[str, str]:
        request = self.request.direct_destinations.get(departureAirportCode=airport_code)
        return request.data
