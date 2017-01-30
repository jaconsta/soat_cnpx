from http import HTTPStatus
import json

from django.test import (Client, TestCase)


class VehicleTestCase(TestCase):
    fixtures = ['vehicle_type.yaml', 'vehicle_classifications.yaml']

    def setUp(self):
        self.client = Client()
        self.url = '/api/v1/vehicle/'
        self.vehicle_fields = ('license_plate', 'vehicle_class', 'vehicle_sub_type', 
                               'model', 'passsenger_capacity', 'cilinders', 'tons')

    def test_vehicle_do_not_exists(self):
        """Review the error response when vehicle do not exists."""
        vehicle_plates = ('XUV645', 'MO506', 'AAA000')

        for vehicle in vehicle_plates:
            # Then GET the vehicles by license plate.
            url = '{0}{1}/'.format(self.url, vehicle)
            resp = self.client.get(self.url)

            # Ensure status 404
            assert resp.status_code == HTTPStatus.NOT_FOUND, \
                        'GET: {url}. Got {error}, Expected {code}'. \
                            format(url=url, error=resp.status_code, code=HTTPStatus.NOT_FOUND.value)

            # Ensure response message corresponds to non-existant licence plates.
            try:
                body = resp.json()
                assert 'not exist' in body['message'], \
                            'GET: {url}. Got content {error}, Expected {code}'. \
                                format(url=url, error=body['message'], code='in *not exists*')
            finally:
                # Because the method is not yet implemented.
                assert False, 'GET: {0}. Response is not JSON type.'.format(url)

    def test_vehicle_exists(self):
        """Review the vehicle existance in the database."""
        # First create vehicles in the database.
        vehicle_data = [
            ('XUV645', '2', '211', 2016, None, 1800, None),
            ('MO506', '1', '130', 2016, None, 1800, None)
            ]
        for vehicle in vehicle_data:
            try:
                # Since vehicle is not yet created.    
                Vehicle.object.create(**dict(zip(self.vehicle_fields, vehicle)))
            except:
                assert False, 'Vehicle is not yet created'

            # Then GET the vehicles by license plate.
            url = '{0}{1}/'.format(self.url, vehicle[0]) 
            resp = self.client.get(self.url)

            # Ensure status 200
            assert resp.status_code == HTTPStatus.OK, \
                        'GET: {url}. Got {error}, Expected {code}'. \
                            format(url=url, error=resp.status_code, code=HTTPStatus.OK.value)

            body = resp.json()
            # Ensure category matches.
            assert body['vehicle_sub_type'] == vehicle[2],  \
                    'GET: {url}. Got category {error}, Expected {code}'. \
                        format(url=url, error=body['vehicle_sub_type'], code=vehicle[2])

    # def test_vehicle_without_soat(self):
    #     ### GOES IN ANOTHER TESTCASE ##
    #     """Validate an existant vehicle does not have soat or it is no longer valid."""

    #     # First create vehicles in the database.
    #     vehicle_data = [
    #         ('XUV645', '2', '211', 2016, None, 1800, None),
    #         ('MO506', '1', '130', 2016, None, 1800, None)
    #         ]
    #     # Create an expired soat.
    #     soat_data = {'MO506': ''}
    #     for vehicle in vehicle_plates:
    #         # Then GET the vehicles by license plate.
    #         url = '[0][1]/'.format(self.url, vehicle[0])
    #         resp = self.client.get(self.url)

    #         # Ensure status 404
    #         assert resp.status_code == HTTPStatus.NOT_FOUND, \
    #                     'GET: {url}. Got {error}, Expected {code}'. \
    #                         format(url=url, error=resp.status_code, code=HTTPStatus.NOT_FOUND.value)

    #         # Ensure response message corresponds to non-existant licence plates.
    #         assert 'not exist' in resp.content, \
    #                     'GET: {url}. Got content {error}, Expected {code}'. \
    #                         format(url=url, error=resp.content, code='in *not exists*')
