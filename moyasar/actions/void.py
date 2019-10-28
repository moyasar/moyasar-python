import moyasar
import json


class Void:
    def void_url(self, id):
        return f'{moyasar.resource_url(self.__class__.__name__)}/{id}/void'.lower()

    def void(self):
        response = moyasar.request('POST', self.void_url(self.id))
        response = json.loads(response.text)
        moyasar.fill_object(self, response)
