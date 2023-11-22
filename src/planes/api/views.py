from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from planes.api.serializers import PlaneSerializer, AttributeSerializer, ValueSerializer
from planes.repositories.repository import PLaneRepository
from planes.api.amadeus_api import Location, amadeus


class PlaneView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        response = amadeus.reference_data.locations.get(
            keyword='LON',
            subType=Location.ANY
        )
        return JsonResponse(response.data, safe=False)
    
    
    # def post(self, request):
    #     code = request.data.get('code', None)
    #     repository = PLaneRepository()
    #     result = repository.create_plane(code)
        
    #     if result:
    #         serializer = PlaneSerializer(result)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response({}, status=status.HTTP_400_BAD_REQUEST)

class AttributeView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        attribute = request.data.get('attribute', None)
        repository = PLaneRepository()
        result = repository.create_atribute(attribute)
        
        if result:
            serializer = AttributeSerializer(result)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

class ValueView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        plane_id = request.data.get('plane_id', None)
        attribute_id = request.data.get('attribute_id', None)
        value = request.data.get('value', None)
        repository = PLaneRepository()
        result = repository.set_value(plane_id, attribute_id, value)
        
        if result:
            serializer = ValueSerializer(result)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
    