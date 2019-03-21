import moyasar
import json
from moyasar.helpers import Constructor


class Create(Constructor):

    @classmethod
    def create_url(cls):
        return f'{moyasar.resource_url(cls.__name__)}'.lower()

    @classmethod
    def create(cls, data):
        response = moyasar.request('POST', cls.create_url(), data)
        response = json.loads(response.text)
        return cls(response)