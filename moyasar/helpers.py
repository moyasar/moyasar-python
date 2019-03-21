import json


class Constructor:

    def __init__(self, data):
        for key in data:
            setattr(self, key, data[key])


class Format:
    def __str__(self):
        return json.dumps(self.__dict__)
