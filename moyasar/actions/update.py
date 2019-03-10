import moyasar


class Update:
    def update_url(self, id):
        return f'{moyasar.resource_url(self.__class__.__name__)}/{id}'.lower()

    def update(self, data):
        response = moyasar.request('PUT', self.update_url(self.id), data)
        return response