from typing import Any, Collection

from drf_spectacular.utils import OpenApiExample, OpenApiParameter, OpenApiTypes


def SelfViewSchema() -> list[Any]:
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


def SelfCreateViewSchema() -> dict[str, dict[str, Collection[str]]]:
    request = {
        'multipart/form-data': {
            'type': 'object',
            'properties': {
                    'code': {'type': 'string', 'example': 'JET321USA262RUS'},
                    'place_code': {'type': 'string', 'example': '10F'},
                    'user_id': {'type': 'string', 'example': '591'},
                    'date': {'type': 'string', 'example': '2024-10-04'}
            }
        }
    }
    return request


def SelfUpdateViewSchema() -> dict[str, dict[str, Collection[str]]]:
    request = {
        'multipart/form-data': {
            'type': 'object',
            'properties': {
                    'code': {'type': 'string', 'example': 'JET321USA262RUS'},
                    'place_code': {'type': 'string', 'example': '10F'},
                    'user_id': {'type': 'string', 'example': '591'},
                    'date': {'type': 'string', 'example': '2024-10-04'}
            }
        }
    }
    return request
