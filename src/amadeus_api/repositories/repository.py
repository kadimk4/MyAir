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

    def predict_travel_pupose(self, city_code_from: str, city_code_to: str, departure_date: str, return_date: str, search_date: str):
        return self.request.predictions.trip_purpose.get(
            originLocationCode=city_code_from,
            destinationLocationCode=city_code_to,
            departureDate=departure_date,
            returnDate=return_date,
            searchDate=search_date
        )
