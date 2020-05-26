from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

#asi es como se importa Micks
from djangoRestFrameworkViewsetPermissions.apipermission import APIPermissionClassFactory


from users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
    APIPermissionClassFactory(
        name='UserPermission',
        permission_configuration={
            'base': {
                'create': True,
                'list': False,
            },
            'instance': {
                'retrieve': lambda user, req: user.is_authenticated,
                'destroy': False,
                'update': lambda user, req: user.is_authenticated,
                'partial_update': lambda user, req: user.is_authenticated,
            }
        }
    ),
)
    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer['password'].value)
        user.save()
        return Response(serializer.data)

    