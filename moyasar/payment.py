from moyasar.resource import Resource
from moyasar.actions.refund import Refund


class Payment(Resource, Refund):
    @classmethod
    def source_to_creditcard(cls, data):
        data.pop('type')
        return CreditCard(**data)

    @classmethod
    def source_to_sadad(cls, data):
        data.pop('type')
        return Sadad(**data)

    @classmethod
    def fix_source(cls, payment):
        if payment.source['type'] == 'creditcard':
            payment.source = cls.source_to_creditcard(payment.source)
        else:
            payment.source = cls.source_to_sadad(payment.source)
        
        return payment

    @classmethod
    def fetch(cls, id):
        payment = super().fetch(id)
        return cls.fix_source(payment)

    @classmethod
    def list(cls, data=None):
        payments = super().list(data)
        fixed_payments = []
        for p in payments:
            fixed_payments.append(cls.fix_source(p))

        return fixed_payments

    def refund(self, amount=None):
        super().refund(amount)
        __class__.fix_source(self)


class Sadad:
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])


class CreditCard:
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
