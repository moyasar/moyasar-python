import moyasar
import json


class Fetch:
    def __init__(self, data):
        for key in data:
            self.__setattr__(key, data[key])

    @classmethod
    def fetch_url(cls, id):
        return f'{moyasar.resource_url(cls.__name__)}/{id}'.lower()

    @classmethod
    def fetch(cls, id):
        response = moyasar.request('GET', cls.fetch_url(id), None)
        response = json.loads(response.text)
        return cls(response)
