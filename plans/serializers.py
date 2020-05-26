from rest_framework import serializers

from plans.models import Plan
from trips.serializers import TripSerializer

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields=(
            'id',
            'name',
            'date',
            'trip'
        )