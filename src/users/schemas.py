from typing import Any, Collection

from drf_spectacular.utils import OpenApiExample, OpenApiParameter, OpenApiTypes


def SelfViewSchema() -> list[Any]:
    parameters = [
        OpenApiParameter(
            name='id',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
            examples=[
                OpenApiExample(
                    name='User ID',
                    value=1261
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
                    'first_name': {'type': 'string', 'example': 'Johnny'},
                    'last_name': {'type': 'string', 'example': 'Sins'},
                    'username': {'type': 'string', 'example': 'johnnysins1978'},
                    'email': {'type': 'string', 'example': 'johnnysinsavia@example.ru'},
                    'link': {'type': 'string', 'example': 'johnny_hub'},
                    'password': {'type': 'string', 'example': 'johnnycool'},
                    'passport': {
                        'type': 'string',
                        'format': 'binary',
                        'example': 'image.jpg'
                    }
            }
        }
    }
    return request


def SelfUpdateViewSchema() -> dict[str, dict[str, Collection[str]]]:
    request = {
        'multipart/form-data': {
            'type': 'object',
            'properties': {
                    'first_name': {'type': 'string', 'example': 'Johnny'},
                    'last_name': {'type': 'string', 'example': 'Sins'},
                    'username': {'type': 'string', 'example': 'johnnysins1978'},
                    'email': {'type': 'string', 'example': 'johnnysinsavia@example.ru'},
                    'link': {'type': 'string', 'example': 'johnny_hub'},
                    'password': {'type': 'string', 'example': 'johnnycool'},
                    'passport': {
                        'type': 'string',
                        'format': 'binary',
                        'example': 'image.jpg'
                    }
            }
        }
    }
    return request
