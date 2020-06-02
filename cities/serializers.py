from rest_framework import serializers

from cities.models import City
from countries.serializers import CountrySerializer

class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields=(
            'id',
            'name',
            'country'
        )
