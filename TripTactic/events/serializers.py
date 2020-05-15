from rest_framework import serializers

from events.models import Event
from places.serializers import PlaceSerializer
from plans.serializers import PlanSerializer

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields=(
            'id',
            'name'
            'hour',
            'description',
            'place',
            'plan'
        )