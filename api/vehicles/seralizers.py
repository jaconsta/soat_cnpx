from rest_framework import serializers

from .models import VehicleType, VehicleClassifications, Vehicle


ERROR_VALUE = 'Incorrect value.'


class VehicleSerializer(serializers.ModelSerializer):
    insurance = serializers.BooleanField(read_only=True, default=False)

    class Meta:
        model = Vehicle
        exclude = ('created_at', 'updated_at',)

    def validate(self, data):
        """
        Validates its sub-type parameters are valid.
        """

        # Validate the possible parametrization combinations.
        if data.get('vehicle_sub_type'):
            # In this field comes in the request, the insurance process straightforward,
            #   Though should validate that all other parameters, if come, are within the
            #   expected ranges.
            vehicle_class = VehicleClassifications.objects.get(data.get('vehicle_sub_type'))

            # Validate parameters match the sub type requirements.
            # Assert the vehicle type matches with the sub-type.
            if not data.get('vehicle_class'):
                data['vehicle_class'] = vehicle_class.vehicle_class
            elif data.get('vehicle_class') != vehicle_class.vehicle_class:
                raise serializers.ValidationError({'vehicle_class': ERROR_VALUE})

            # Validate that options match the vehicle type required.
            type_measure = vehicle_class.vehicle_type.measurement

            if type_measure == VehicleType.CUBIC_CENTIMETERS and data.get('cylinders'):
                cc = data.get('cylinders')

                if (vehicle_class.th_meas_max or 0) > cc > (vehicle_class.th_meas_min or 0):
                    raise serializers.ValidationError({'cylinders': ERROR_VALUE})

            elif type_measure == VehicleType.PASSENGERS and data.get('passenger_capacity'):
                passengers = data.get('passenger_capacity')

                if (vehicle_class.th_meas_max or 0) > passengers > (vehicle_class.th_meas_min or 0):
                    raise serializers.ValidationError({'passenger_capacity': ERROR_VALUE})

            elif type_measure == VehicleType.TONS and data.get('tons'):
                tons = data.get('tons')

                if (vehicle_class.th_meas_max or 0) > tons > (vehicle_class.th_meas_min or 0):
                    raise serializers.ValidationError({'tons': ERROR_VALUE})

            elif type_measure == VehicleType.TONS and data.get('tons'):
                tons = data.get('tons')

                if (vehicle_class.th_meas_max or 0) > tons > (vehicle_class.th_meas_min or 0):
                    raise serializers.ValidationError({'tons': ERROR_VALUE})

        return data
