from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from usersFeedBacK.models import UserFeedback
from usersFeedBacK.serializers import UserFeedBackSerializer

class UserFeedBackViewSet(viewsets.ModelViewSet):
    queryset = UserFeedback.objects.all()
    serializer_class = UserFeedBackSerializer