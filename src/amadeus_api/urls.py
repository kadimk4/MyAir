from django.urls import path

from amadeus_api.api.views import SelfView, SelfViewAirport_direct, SelfViewCheapest_flights, SelfViewCheapest_journey, SelfViewCheckin_links, SelfViewDetails_airport, SelfViewFavorable_flights_dates, SelfViewList_city_hotels, SelfViewList_near_airports, SelfViewPercentage_ofontime_departures, SelfViewPredict_flight_delay, SelfViewPredict_travel_choice, SelfViewPredict_travel_purpose, SelfViewRecommended_locations
from rest_framework import routers
urlpatterns = [
    path('amadeus/', SelfView.as_view(), name='amadeus-view'),
    path('amadeus/cheapest_flights/<str:city_code>', SelfViewCheapest_flights.as_view(), name='cheapest_flights'),
    path('amadeus/favorable_flights_dates/<str:city_code_from>/<str:city_code_to>', SelfViewFavorable_flights_dates.as_view(), name='favorable_flights_dates'),
    path('amadeus/cheapest_journey/<str:city_code_from>/<str:city_code_to>/<str:date>/<str:adults_count>',SelfViewCheapest_journey.as_view(), name='cheapest_journey'),
    path('amedeus/predict_travel_choice/<str:city_code_from>/<str:city_code_to>/<str:date>/<str:adults_count>', SelfViewPredict_travel_choice.as_view(), name='predict_travel_choice'),
    path('amadeus/predict_travel_purpose/<str:city_code_from>/<str:city_code_to>/<str:departure_date>/<str:arrival_date>/<str:search_date>', SelfViewPredict_travel_purpose.as_view(), name='predict_travel_purpose'),
    path('amadeus/predict_flight_delay/<str:city_code_from>/<str:city_code_to>/<str:departure_date>/<str:departure_time>/<str:arrival_date>/<str:arrival_time>/<str:aircraft_code>/<str:carrier_code>/<str:flight_number>/<str:duration>', SelfViewPredict_flight_delay.as_view(), name='predict_flight_delay'),
    path('amadeus/details_airport/<str:airport_code>', SelfViewDetails_airport.as_view(), name='details_airport'),
    path('amadeus/list_near_airports/<str:longitude>/<str:latitude>', SelfViewList_near_airports.as_view(), name='list_near_airports'),
    path('amadeus/checkin_links/<str:airline_code>/<str:language>', SelfViewCheckin_links.as_view(), name='checkin_links'),
    path('amadeus/recommended_locations/<str:city_code>/<str:country_code>', SelfViewRecommended_locations.as_view(), name='recommended_locations'),
    path('amadeus/percentage_ofontime_departures/<str:airport_code>/<str:date>', SelfViewPercentage_ofontime_departures.as_view(), name='percentage_ofontime_departures'),
    path('amadeus/airport_direct/<str:airport_code>', SelfViewAirport_direct.as_view(), name='airport_direct'),
]
