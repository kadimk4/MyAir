from amadeus import Client, Location

from app.settings import AVIA_API_KEY, AVIA_SECRET_KEY

amadeus = Client(
    client_id=AVIA_API_KEY,
    client_secret=AVIA_SECRET_KEY
)