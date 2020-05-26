from rest_framework import serializers

from transportProviders.models import TransportProvider

class TransportProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportProvider
        fields=(
            'id',
            'name'
        )