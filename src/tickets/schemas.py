from drf_spectacular.utils import OpenApiParameter, OpenApiTypes, OpenApiExample

def SelfViewSchema() -> list[str, any]:
    parameters=[
            OpenApiParameter(
                name="ticket_id",
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

def SelfCreateViewSchema() -> dict[str, any]:
    request={
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

def SelfUpdateViewSchema() -> dict[str, dict[str, str]]:
    request={
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
