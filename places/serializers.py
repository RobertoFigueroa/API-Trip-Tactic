from rest_framework import serializers

from places.models import Place
from cities.serializers import CitySerializer

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields=(
            'id',
            'name',
            'place_type',
            'description',
            'city'
        )