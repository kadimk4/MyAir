from amadeus_api.repositories.repository import AirportRepository, ReferenceDataRepository, ShoppingRepository, TravelRepository
from core.interface import BaseRepository
from tickets.repositories.repository import TicketRepository
from users.repositories.repository import UserRepository


class RepositoryFactory:
    repositories: dict[str, type[BaseRepository]] = {'user': UserRepository,
                                                    'ticket': TicketRepository,
                                                    'amadeus_travel': TravelRepository,
                                                    'amadeus_shopping': ShoppingRepository,
                                                    'amadeus_reference': ReferenceDataRepository,
                                                    'amadeus_airport': AirportRepository
                                                    }

    @classmethod
    def create(cls, name: str) -> BaseRepository:
        if name in cls.repositories:
            return cls.repositories[name]()
        raise ValueError('Repository not found: %s' % name)
