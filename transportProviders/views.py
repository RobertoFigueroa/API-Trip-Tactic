from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from transportProviders.models import TransportProvider
from transportProviders.serializers import TransportProviderSerializer

class TransportProviderViewSet(viewsets.ModelViewSet):
    queryset = TransportProvider.objects.all()
    serializer_class = TransportProviderSerializer
