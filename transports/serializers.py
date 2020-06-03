from rest_framework import serializers

from transports.models import Transport
from transportProviders.serializers import TransportProviderSerializer
from countries.serializers import CountrySerializer


class TranportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields=(
	    'id',
            'transport_type',
            'price',
            'transportProvider',
            'destination'
        )
