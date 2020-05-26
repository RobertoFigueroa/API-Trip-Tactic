from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from guardian.shortcuts import assign_perm

from djangoRestFrameworkViewsetPermissions.apipermission import APIPermissionClassFactory


from trips.models import Trip
from trips.serializers import TripSerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = (
    APIPermissionClassFactory(
        name='TripPermissions',
        permission_configuration={
            'base': {
                'create': True,
                'list': False,
                'getMyTrips':  True,

            },
            'instance': {
                'getMyTrips':  True,
                'retrieve': "trips.view_trip",
                'destroy': 'trips.delete_trip',
                'update': 'trips.change_trip',
                'partial_update': 'trips.change_trip',
            }
        }
    ),
)

    def perform_create(self, serializer):
        trip = serializer.save()
        user = self.request.user
        assign_perm('trips.view_trip', user, trip)
        assign_perm('trips.change_trip', user, trip)
        assign_perm('trips.delete_trip', user, trip)
        trip.save()
        return Response(serializer.data)

    @action(detail=False, url_path='my-trips', methods=['get'])
    def getMyTrips(self, request):
        myTrips = []
        user = self.request.user
        for trip in Trip.objects.all():
            print(TripSerializer(trip).data)
            if user.has_perm('view_trip',trip):
                myTrips.append(TripSerializer(trip).data)
        return Response(myTrips)