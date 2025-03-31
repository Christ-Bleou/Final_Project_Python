from django.shortcuts import render

from rest_framework import viewsets
from api.serializer import OeuvreSerializer, LocationSerializer
from ecommerce.models import Oeuvre, Location

class OeuvreViewSet(viewsets.ModelViewSet):
    queryset = Oeuvre.objects.all()
    serializer_class = OeuvreSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
