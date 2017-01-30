from django.db import models


class VehicleType(models.Model):
    # Main vehicle category
    name = models.CharField(max_length= 150)
    # Measurement units to calculate limits
    CUBIC_CENTIMETERS = "cc"
    TONS = 'T'
    PASSENGERS = 'P'
    NONE = 'N'
    measurement_choices= (
        (CUBIC_CENTIMETERS, 'c.c.'),
        (TONS, 'Toneladas'),
        (PASSENGERS, 'Pasajeros'),
        (NONE, 'Ninguna'),
    )
    measurement = models.CharField(max_length=10, choices=measurement_choices)

    def str(self):
        return self.name


class VehicleClassifications(models.Model):
    # Unique code assignment .
    code = models.IntegerField()
    # Main category.
    vehicle_class = models.ForeignKey('VehicleType')

    # Sub-category definition.
    # Null field excludes that limit
    # MEASurement thresholds: minimum / maximum values.
    th_meas_min = models.IntegerField(null=True, blank=True)
    th_meas_max = models.IntegerField(null=True, blank=True)
    # If both are null, it can have a special name.
    meas_spec_name = models.CharField(max_length=50, null=True, blank=True)

    # Years usage thresholds.
    # If both are null years wont apply.
    year_min = models.IntegerField(null=True, blank=True)
    year_max = models.IntegerField(null=True, blank=True)

    # Base for commerzial charges.
    # According to fasecolda
    # http://www.fasecolda.com/files/1114/8406/4009/Tarifas_soat_2016C004-09.pdf
    # Tasa comercial (CE04-09 SFC
    commercial_fee = models.FloatField()
    # Valor prima
    base_value = models.IntegerField()
