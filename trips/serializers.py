from rest_framework import serializers

from trips.models import Trip
from users.serializers import UserSerializer

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields=(
            'id',
            'name',
            'description',
            'user'
        )