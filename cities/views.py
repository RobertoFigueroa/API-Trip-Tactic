from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action



from cities.models import City
from cities.serializers import CitySerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
