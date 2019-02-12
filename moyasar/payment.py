from moyasar.resource import Resource
from moyasar.actions.refund import Refund


class Source:
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @classmethod
    def build(cls, payment):
        if payment.source['type'] == "creditcard":
            payment.source = CreditCard.source_to_creditcard(payment.source)
        else:
            payment.source = Sadad.source_to_sadad(payment.source)
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

    @classmethod
    def fetch(cls, id):
        payment = super().fetch(id)
        return Source.build(payment)

    @classmethod
    def list(cls, data=None):
        payments = super().list(data)
        fixed_payments = []
        for p in payments:
            fixed_payments.append(Source.build(p))

        return fixed_payments

    def refund(self, amount=None):
        super().refund(amount)
        __class__.build(self)
