from rest_framework import serializers

from .models import Citizen


class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        exclude = ('created_at', 'updated_at',)