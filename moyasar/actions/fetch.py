import moyasar
import json


class Fetch:
    @classmethod
    def fetch_url(cls, id):
        return f'{moyasar.resource_url(cls.__name__)}/{id}'.lower()

    @classmethod
    def fetch(cls, id):
        response = moyasar.request('GET', cls.fetch_url(id), None)
        response = json.loads(response.text)
        resource = cls()
        moyasar.fill_object(resource, response)
        return resource
