import moyasar
import json


class Update:
    def update_url(self, id):
        return f'{moyasar.resource_url(self.__class__.__name__)}/{id}'.lower()

    def update(self, data):
        moyasar.request('PUT', self.update_url(self.id), data)
