import moyasar
import json
from moyasar.constructor import Constructor


class Create(Constructor):
    def __init__(self, data):
        super().__init__(**data)


    @classmethod
    def create_url(cls):
        return f'{moyasar.resource_url(cls.__name__)}'.lower()

    @classmethod
    def create(cls, data):
        response = moyasar.request('POST', cls.create_url(), data)
        response = json.loads(response.text)
        return cls(response)
