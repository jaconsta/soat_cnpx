from rest_framework import serializers

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    insurance = serializers.BooleanField(read_only=True, default=False)

    class Meta:
        model = Vehicle
        exclude = ('created_at', 'updated_at',)

    def validate(self, data):
        """
        Validaets its sub-type parameters are valid.
        """

        # Validate the possible parametrization combinations.
        pass