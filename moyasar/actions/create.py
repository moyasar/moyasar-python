import moyasar
import json


class Create:
    @classmethod
    def create_url(cls):
        return f'{moyasar.resource_url(cls.__name__)}'.lower()

    @classmethod
    def create(cls, data):
        response = moyasar.request('POST', cls.create_url(), data)
        response = json.loads(response.text)
        resource = cls()
        moyasar.fill_object(resource, response)
        return resource
