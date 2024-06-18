from typing import Any, Collection

from drf_spectacular.utils import OpenApiExample, OpenApiParameter, OpenApiTypes


def SelfViewSchemaID() -> list[Any]:
    parameters = [
        OpenApiParameter(
            name='ticket_id',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
            examples=[
                OpenApiExample(
                    name='Ticket ID',
                    value=5126
                )
            ],
            required=True
        )
    ]
    return parameters


def SelfViewSchema() -> dict[str, dict[str, Collection[str]]]:
    request = {
        'multipart/form-data': {
            'type': 'object',
            'properties': {
                    'code': {'type': 'string', 'example': 'ECOUXOPO1145RUS'},
                    'departure_date': {'type': 'string', 'example': '2024-11-11'},
                    'duration': {'type': 'string', 'example': '01:30:00'},
                    'price': {'type': 'string', 'example': '52'},
                    'user_id': {'type': 'string', 'example': '591'},
            }
        }
    }
    return request

def SelfAMADEUSViewSchema() -> dict[str, dict[str, Collection[str]]]:
    request = {
        'multipart/form-data': {
            'type': 'object',
            'properties': {
                    'date': {'type': 'string', 'example': '2024-11-11'},
                    'city_code_from': {'type':'string', 'example': 'MAD'},
                    'city_code_to': {'type':'string', 'example': 'OPO'},
                    'adults_count': {'type':'string', 'example': '1'},
            }
        }
    }
    return request