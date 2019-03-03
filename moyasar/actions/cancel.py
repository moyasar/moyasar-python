import moyasar
import json


class Cancel:
    def cancel_url(self, id):
        return f'{moyasar.resource_url(self.__class__.__name__)}/{id}/cancel'.lower()

    def cancel(self):
        response = moyasar.request('PUT', self.cancel_url(self.id), None)
        response = json.loads(response.text)
        moyasar.fill_object(self, response)
        return response
