from moyasar.resource import Resource
from moyasar.actions.refund import Refund
import pdb


class Source:
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @classmethod
    def build(cls, source):
        if source['type'] == "creditcard":
            Source.source_to_creditcard(source)
        else:
            Source.source_to_sadad(source)

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


class Payment(Resource, Refund, Source):

    @classmethod
    def fetch(cls, id):
        payment = super().fetch(id)
        payment.source = Source.build(payment.source)
        return payment

    @classmethod
    def list(cls, data=None):
        payments = super().list(data)
        fixed_payments = []
        for p in payments:
            p.source = Source.build(p.source)
            fixed_payments.append(p)
        return fixed_payments

    def refund(self, amount=None):
        super().refund(amount)
        __class__.build(self.source)
        return self
