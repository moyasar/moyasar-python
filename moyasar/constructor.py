class Constructor:

    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
