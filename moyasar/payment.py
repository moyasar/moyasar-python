from moyasar.resource import Resource
from moyasar.actions.refund import Refund
from moyasar.constructor import Constructor


class Source(Constructor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def build(cls, source):
        if source['type'] == "creditcard":
            source = Source.source_to_creditcard(source)
        else:
            source = Source.source_to_sadad(source)
        return source

    @classmethod
    def source_to_creditcard(cls, data):
        data.pop('type')
        return CreditCard(**data)

    @classmethod
    def source_to_sadad(cls, data):
        data.pop('type')
        return Sadad(**data)


class CreditCard(Source):
    pass


class Sadad(Source):
    pass


class Payment(Resource, Refund):
    def __init__(self, data):
        super().__init__(data)
        self.source = Source.build(self.source)

    def refund(self, amount=None):
        super().refund(amount)
        self.source = Source.build(self.source)
        return self
