from http import HTTPStatus
import json

from django.test import (Client, TestCase)

from citizens.models import Citizen

class CitizensTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/api/v1/citizen/'
        self.citizen_fields = ('name', 'last_name', 'email', 'phone', 
                          'document_type', 'document_number')
        self.citizen_datas = [
            ('first', 'soat one', 'soat.one@mailinator.com', '57313123467', 
             'CC', 54123456),
            ('second', 'soat two', 'soat.two@mailinator.com', '57315345673',
             'PP', 89765411)
        ]

    def test_create(self):
        """ Should create an user and send it back in reponse."""
        for citizen in self.citizen_datas:
            # Request the citizen creation.
            body = dict(zip(self.citizen_fields, citizen))

            resp = self.client.post(self.url, data=json.dumps(body), content_type='application/json')

            # Ensure estatus 201
            assert resp.status_code == HTTPStatus.CREATED, \
                    '{url}: Got {error}, Expected {code}'. \
                        format(url=self.url, error=resp.status_code, code=HTTPStatus.CREATED.value)

            resp_body = resp.json()
            # Ensure data created is correct.
            for key in body:
                assert resp_body[key] == body[key], \
                    '{url}: Got field {field} -> {error}, Expected {code}'. \
                        format(url=self.url, field = key, error=resp_body[key], code=body[key])


    def test_get_all(self):
        """ Should return many users created."""
        # Create citizens in the database.
        for citizen in self.citizen_datas:
            Citizen.objects.create(**dict(zip(self.citizen_fields, citizen)))

        # Ensure status 200.
        resp = self.client.get(self.url)
        assert resp.status_code == HTTPStatus.OK, \
                    'GET: {url}. Got {error}, Expected {code}'. \
                        format(url=self.url, error=resp.status_code, code=HTTPStatus.OK.value)

        # Ensure body data type.
        body = resp.json()
        assert type(body) is list,  \
                    'GET: {url}. Got type {error}, Expected {code}'. \
                        format(url=self.url, error=type(body), code='list')
        # Ensure there are no more records than the created.
        assert len(body) is len(self.citizen_datas),  \
                    'GET: {url}. Got length {error}, Expected {code}'. \
                        format(url=self.url, error=len(body), code=len(self.citizen_datas))


    def test_get_one(self):
        """ Should return many users created."""
        
        citizen_ids = list()

        for citizen in self.citizen_datas:
            # Create the citize in the database.
            body = dict(zip(self.citizen_fields, citizen))
            person = Citizen.objects.create(**body)

            # Get the citizen from it's Id.
            url = '{0}{1}/'.format(self.url, person.id)
            resp = self.client.get(url)
            # Ensure status 200.
            assert resp.status_code == HTTPStatus.OK, \
                        'GET: {url}. Got {error}, Expected {code}'. \
                            format(url=self.url, error=resp.status_code, code=HTTPStatus.OK.value)

            resp_body = resp.json()
            for key in body:
                # Ensure each field in the response has the correct data.
                assert resp_body[key] == body[key], \
                    '{url}: Got field {field} -> {error}, Expected {code}'. \
                        format(url=url, field = key, error=resp_body[key], code=body[key])
