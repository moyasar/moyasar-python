import moyasar
import json


class Create:
    def __init__(self, data):
        for key in data:
            self.__setattr__(key, data[key])

    @classmethod
    def create_url(cls):
        return f'{moyasar.resource_url(cls.__name__)}'.lower()

    @classmethod
    def create(cls, data):
        response = moyasar.request('POST', cls.create_url(), data)
        response = json.loads(response.text)
        return cls(response)
