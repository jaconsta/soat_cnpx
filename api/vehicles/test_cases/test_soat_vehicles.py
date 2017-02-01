import datetime
from http import HTTPStatus
import json

from django.test import (Client, TestCase)

from vehicles.models import Vehicle, Insurance


class SoatTestCase(TestCase):
    """
    Test of vehicles with valid Soat.
    Basically extends test_vehicles_crud by validating the insurance exists attibute.

    """
    def setup(self):
        # Base configuration
        self.client = Client()
        self.url = '/api/v1/vehicle'

        # DB fields
        self.vehicle_fields = ('license_plate', 'vehicle_class', 'vehicle_sub_type', 
                               'model', 'passsenger_capacity', 'cilinders', 'tons')
        self.vehicle_data = (
            ('XUV645', '2', '211', 2016, None, 1800, None),
            ('MO506', '1', '130', 2016, None, 1800, None))

        self.insurance_fields = ('vehicle', 'purchase_date', 'valid_from')

        # Create the vehicles.
        for vehicle in vehicle_data:
            Vehicle.objects.create(**dict(zip(self.vehicle_fields, vehicle)))

    def test_no_insurance(self):
        """None of the vehicles has bought its insurance."""
        for vehicle in vehicle_data:
            # Get the vehicle information.
            url = '{0}{1}/'.format(self.url, vehicle[0])
            resp = self.client.get(url)

            # Ensure the status 200
            assert resp.status_code is HTTPStatus.OK, \
                        'GET: {url}. Got {error}, Expected {code}'. \
                            format(url=url, error=resp.status_code, code=HTTPStatus.OK.value)

            body = resp.json()
            # Ensure that data corresponds to the same vechicle
            for index in range(2):  # With the first two is enough
                field = vehicle_fields[index]
                assert body[field] == vehicle[indez],  \
                        'GET: {url}. Got {field} {error}, Expected {code}'. \
                            format(url=url, field=field, error=body[field], code=vehicle[2])

            # Ensure both have no insurance
            assert body['insurance'] == False,  \
                    'GET: {url}. Got insurance {error}, Expected {code}'. \
                        format(url=url, error=body['insurance'], code='False')

    def test_with_expired_insurance(self):
        """Should show that even if the vehicle has bought insurance it has expired."""
        # First create the expired insurances in the database.
        insurance_data = (
            (1, datetime.date(2015, 1, 1), datetime.date(2015, 1, 1)),  # This is expired
            (2, datetime.date(2018, 1, 1), datetime.date(2018, 1, 1)),) # Somehow it starts in the future.
        for insurance in insurance_data:
            Insurance.objects.create(insurance)

        # Validate insurance status.
        for vehicle in vehicle_data:
            url = '{0}{1}/'.format(self.url, vehicle[0])

            # Get the vehicle data.
            resp = self.client.get(url)

            # Ensure status 200.
            assert resp.status_code == HTTPStatus.OK, \
                        'GET: {url}. Got {error}, Expected {code}'. \
                            format(url=url, error=resp.status_code, code=HTTPStatus.OK.value)

            body = resp.json()
            # Ensure the insurance is expired or not valid.
            assert body['insurance'] == False,  \
                    'GET: {url}. Got insurance {error}, Expected {code}'. \
                        format(url=url, error=body['insurance'], code='False') 

    def test_with_valid_insurance(self):
        """Should show the vehicle has a valid insurance."""
        # First create the expired insurances in the database.
        insurance_data = (
            (1, datetime.date(2016, 6, 1), datetime.date(2016, 6, 1)), 
            (2, datetime.datetime.now(), datetime.datetime.now()),) 
        for insurance in insurance_data:
            Insurance.objects.create(insurance)

        # Validate insurance status.
        for vehicle in vehicle_data:
            url = '{0}{1}/'.format(self.url, vehicle[0])

            # Get the vehicle data.
            resp = self.client.get(url)

            # Ensure status 200.
            assert resp.status_code == HTTPStatus.OK, \
                        'GET: {url}. Got {error}, Expected {code}'. \
                            format(url=url, error=resp.status_code, code=HTTPStatus.OK.value)

            body = resp.json()
            # Ensure the insurance is expired or not valid.
            assert body['insurance'] == True,  \
                    'GET: {url}. Got insurance {error}, Expected {code}'. \
                        format(url=url, error=body['insurance'], code='True') 

