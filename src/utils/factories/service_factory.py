from typing import Any

from apps.amadeus_api.services.service import (
    AirportService,
    ReferenceDataService,
    ShoppingService,
    TravelService,
)
from apps.auth.serializers import AuthSerializer


class ServiceFactory:
    repositories: dict[str, Any] = {'amadeus_travel': TravelService, 'amadeus_shopping': ShoppingService,
                                    'amadeus_reference': ReferenceDataService, 'amadeus_airport': AirportService, 'auth': AuthSerializer}

    @classmethod
    def create(cls, name: str) -> Any:
        if name in cls.repositories:
            return cls.repositories[name]()
        raise ValueError('Repository not found: %s' % name)
