from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from plans.models import Plan
from plans.serializers import PlanSerializer

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer