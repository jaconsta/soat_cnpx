from rest_framework import viewsets
from rest_framework.response import Response

from .models import Citizen
from .serializers import CitizenSerializer


class CitizenViewSet(viewsets.ModelViewSet):
	""" Citizen manager"""
	queryset = Citizen.objects.all()
	serializer_class = CitizenSerializer
