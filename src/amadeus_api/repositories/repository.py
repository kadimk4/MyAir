from amadeus import Hotel
from api.main import amadeus


class ShoppingRepository:

    def __init__(self) -> None:
        self.request = amadeus.shopping

    def cheapest_flights(self, city_code: str):
        return self.request.flight_destinations.get(origin=city_code)

    def favorable_flights_dates(self, city_code_from: str, city_code_to: str):
        return self.request.flight_dates.get(origin=city_code_from, destination=city_code_to)

    def cheapest_journey(self, city_code_from: str, city_code_to: str, date: str, adults_count: int):
        self.request.flight_offers_search.get(
            originLocationCode=city_code_from,
            destinationLocationCode=city_code_to,
            departureDate=date,
            adults=adults_count
        )

    def predict_travel_choice(self, city_code_from: str, city_code_to: str, date: str, adults_count: int):
        return self.request.flight_offers.prediction.post(self.cheapest_journey(city_code_from, city_code_to, date, adults_count))

    def available_seats(self, body):
        return self.request.availability.flight_availabilities.post(body)


class TravelRepository:

    def __init__(self) -> None:
        self.request = amadeus.travel

    def predict_travel_pupose(self, city_code_from: str, city_code_to: str, departure_date: str, arrival_date: str, search_date: str):
        return self.request.predictions.trip_purpose.get(
            originLocationCode=city_code_from,
            destinationLocationCode=city_code_to,
            departureDate=departure_date,
            returnDate=arrival_date,
            searchDate=search_date
        )

    def predinct_flight_delay(self, city_code_from: str, city_code_to: str, departure_date: str, departure_time: str, arrival_date: str, arrival_time: str, aircraft_code: str, carrier_code: str, flight_number: str, duration: str):
        return self.request.predictions.flight_delay.get(
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


class ReferenceDataRepository:

    def __init__(self) -> None:
        self.request = amadeus.reference_data

    def details_airport(self, airport_code: str):
        return self.request.location(airport_code).get()

    def list_near_airports(self, longitude: float, latitude: float):
        return self.request.locations.airports.get(longitude=longitude, latitude=latitude)

    def checkin_links(self, airline_code: str, language: str = 'en-GB'):
        return self.request.urls.checkin_links.get(airlineCode=airline_code, language=language)

    def recommended_locations(self, city_code: str, country_code: str):
        return self.request.recommended_locations.get(cityCodes=city_code, travelerCountryCode=country_code)

    def list_city_hotels(self, city_code: str):
        return self.request.locations.hotel.get(keyword=city_code, subType=[Hotel.HOTEL_LEISURE, Hotel.HOTEL_GDS])


class AirportRepository:

    def __init__(self) -> None:
        self.request = amadeus.airport

    def percentage_ofontime_departures(self, airport_code: str, date: str):
        return self.request.predictions.on_time.get(airportCode=airport_code, date=date)

    def airport_direct(self, airport_code: str):
        return self.request.direct_destinations.get(airport_code)
