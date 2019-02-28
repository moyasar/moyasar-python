import moyasar
import json


class List:
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
            r = cls()
            moyasar.fill_object(r, resource)
            resource_list.append(r)

        return resource_list
