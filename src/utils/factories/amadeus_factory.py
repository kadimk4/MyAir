from typing import Any

from apps.amadeus_api.repositories.repository import (
    AirportRepository,
    ReferenceDataRepository,
    ShoppingRepository,
    TravelRepository,
)


class AmadeusFactory:
    repositories: dict[str, Any] = {'amadeus_travel': TravelRepository, 'amadeus_shopping': ShoppingRepository,
                                    'amadeus_reference': ReferenceDataRepository, 'amadeus_airport': AirportRepository}

    @classmethod
    def create(cls, name: str) -> Any:
        if name in cls.repositories:
            return cls.repositories[name]()
        raise ValueError('Repository not found: %s' % name)
