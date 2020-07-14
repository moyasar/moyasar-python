import json

from moyasar.resource import Resource
from moyasar.actions.refund import Refund
from moyasar.actions.capture import Capture
from moyasar.actions.void import Void
from moyasar.helpers import Constructor, Format


class Source(Constructor, Format):
    @classmethod
    def build(cls, source):
        source_klass = sources[source.pop('type')]
        return source_klass(source)


class CreditCard(Source):
    def __str__(self):
        return json.dumps(self.__dict__)

class Sadad(Source):
    pass

class ApplePay(Source):
    pass

class STCPay(Source):
    pass

sources = {
    'creditcard': CreditCard,
    'sadad': Sadad,
    'applepay': ApplePay,
    'stcpay': STCPay,
}


class Payment(Resource, Refund, Capture, Void, Format):
    def __init__(self, data):
        super().__init__(data)
        self.source = Source.build(self.source)

    def refund(self, amount=None):
        super().refund(amount)
        self.source = Source.build(self.source)
        return self

    def capture(self, amount=None):
        super().capture(amount)
        self.source = Source.build(self.source)
        return self

    def void(self):
        super().void()
        self.source = Source.build(self.source)
        return self
