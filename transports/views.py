from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from transports.models import Transport
from transports.serializers import TranportSerializer

class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TranportSerializer