class Constructor:

    def __init__(self, data):
        for key in data:
            setattr(self, key, data[key])
