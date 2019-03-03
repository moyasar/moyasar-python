from moyasar.resource import Resource
from moyasar.actions.refund import Refund
from moyasar.constructor import Constructor


class Source(Constructor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def build(cls, payment):
        if payment.source['type'] == "creditcard":
            payment.source = Source.source_to_creditcard(payment.source)
        else:
            payment.source = Source.source_to_sadad(payment.source)
        return payment

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
        Source.build(self)

    def refund(self, amount=None):
        super().refund(amount)
        __class__.build(self)
