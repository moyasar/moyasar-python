import moyasar
import json
from moyasar.helpers import Constructor


class Fetch(Constructor):

    @classmethod
    def fetch_url(cls, id):
        return f'{moyasar.resource_url(cls.__name__)}/{id}'.lower()

    @classmethod
    def fetch(cls, id):
        response = moyasar.request('GET', cls.fetch_url(id), None)
        response = json.loads(response.text)
        return cls(response)
