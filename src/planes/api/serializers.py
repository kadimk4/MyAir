from rest_framework import serializers

from planes.models import Plane

class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = [
            'id',
            'code',
        ]

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = [
            'id',
            'name',
        ]

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = [
            'id',
            'plane_id',
            'attribute_id',
            'value',
        ]
