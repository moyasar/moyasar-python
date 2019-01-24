"""This is the payment module.

This module contains a payment class to accomplish the Moyasar payment service.
"""

from http_ import http_client
from http_ import urls

class Payment:

    def __init__(self, instance_id):
        self.instance_id = instance_id

    @staticmethod
    def create_payment( _params=None):
        try:
            http_client.HttpClient.request(method="post", _url=urls.create_payment_url(), arguments=_params)
        except Exception as e:
            print(e)



    def fetch_payment(self):
        try:
            http_client.HttpClient.request(method="get", _url= urls.fetch_payment_url(self.instance_id),arguments=None)
        except Exception as e:
            return e

    def refund_payment(self):
        try:
            pass
        except Exception as e:
            return e

    def update_payment(self):
        try:
            pass
        except Exception as e:
            return e

    @staticmethod
    def list_payments():
        try:
            pass
        except Exception as e:
            return e







# Payment.create({"amount":300,"currency": "SAR","source": {
#                           "type":   "creditcard",
#                           "name":   "Abdulaziz Nasser",
#                           "number": "4111111111111111",
#                           "cvc":    331,
#                           "month":  12,
#                           "year":   2021
#                         }})

# Payment.create_payment({"amount":300,"currency": "SAR","source": {"type":   "creditcard", "name":   "Abdulaziz Nasser", "number": "4111111111111111",  "cvc":    331, "month":  12, "year":   2021  }})

p = Payment('cc3886a6-71b7-477b-9fde-8d11b20a4ecd')
print(p.fetch_payment())