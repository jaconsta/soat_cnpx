import datetime

from django.db import models
from django.utils import timezone

from .services import years_ago


class VehicleType(models.Model):
    """Main vehicle classes available"""
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

    # For monitoring purpose.
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return self.name


class VehicleClassifications(models.Model):
    """Parametrization of the vehicle classifications."""
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

    # For monitoring purpose.
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return '{code}, Class. {vehicle_class}'.format(code=self.code, vehicle_class=self.vehicle_class.name)


class Vehicle(models.Model):
    """Vehicle registered in the system."""
    license_plate = models.CharField(max_length=10, unique=True)

    # Classification based on the parametrization tables.
    vehicle_class = models.ForeignKey('VehicleClassifications') # This field might be redundant.
    vehicle_sub_type = models.ForeignKey('VehicleClassifications')

    # Details of the vehicle, based on the VehicleClassifications parameters.
    # Year the vehicle was bought.
    model = models.IntegerField()
    # Passengers capacity.
    passsenger_capacity = models.IntegerField()
    # Total CC of the vehicle.
    cilinders = models.IntegerField()
    # Load capacity in tons.
    tons = models.IntegerField()
    
    # For monitoring purpose.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def years_old(self):
        return years_ago(self.model)

    

class Insurance(models.Model):
    """
    The insurance taken by the vehicle.
    Should have it's own APP.
    """
    vehicle = models.ForeignKey('Vehicle')

    # Insurance details.
    insurance_type = models.CharField(max_length=50, default='soat')
    purchase_date = models.DateTimeField(default=timezone.now())

    # Date it starts to be valid.
    valid_from = models.DateField(default=datetime.datetime.today())

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

