import moyasar
import json
from moyasar.constructor import Constructor


class Fetch(Constructor):
    def __init__(self, data):
        super().__init__(data)

    @classmethod
    def fetch_url(cls, id):
        return f'{moyasar.resource_url(cls.__name__)}/{id}'.lower()

    @classmethod
    def fetch(cls, id):
        response = moyasar.request('GET', cls.fetch_url(id), None)
        response = json.loads(response.text)
        return cls(response)
