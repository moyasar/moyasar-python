import json


class Constructor:
    def __init__(self, data):
        for key in data:
            setattr(self, key, data[key])


class Format:
    def __str__(self):
        dict = self.__dict__
        for key in dict:
            if isinstance(dict[key], Format):
                dict[key] = dict[key].__dict__
        return json.dumps(self.__dict__)
