import moyasar
import json
from moyasar.constructor import Constructor


class List(Constructor):
    def __init__(self, data):
        super().__init__(data)

    @classmethod
    def list_url(cls):
        return f'{moyasar.resource_url(cls.__name__)}'.lower()

    @classmethod
    def list(cls, data=None):
        response = moyasar.request('GET', cls.list_url(), data)
        response = json.loads(response.text)
        field_name = f'{cls.__name__}s'.lower()
        resource_list = []
        for resource in response[field_name]:
            resource_list.append(cls(resource))

        return resource_list
