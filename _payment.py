"""This is the payment module.
This module contains Payment class that inherits Moyasar class.
Payment class contains static and instance methods to perform moyasar operations,
and these methods are:
create_payment(arguments, my_key), fetch_payment(self, my_key), refund_payment(self, arguments, my_key),
update_payment(self,arguments, my_key), list_payments(my_key)
"""

from http_ import http_client
from http_ import urls
from moyasar import Moyasar
from errors import BuiltInExceptions as be
from globals import sentinel

class Payment(Moyasar):


    def __init__(self, instance_id):
        self.instance_id = instance_id

    @staticmethod
    def create_payment(arguments, my_key = sentinel):
        be.key_error(my_key)
        try:
            response = http_client.HttpClient.request(method="post", _url=urls.create_payment_url(), arguments=arguments, _key= my_key)
            return response
        except Exception as e:
            return e



    def fetch_payment(self, my_key = sentinel):
        be.key_error(my_key)
        try:
            response = http_client.HttpClient.request(method="get", _url= urls.fetch_payment_url(self.instance_id), _key= my_key)
            return response
        except Exception as e:
            return e

    def refund_payment(self, arguments, my_key = sentinel):
        be.key_error(my_key)
        try:
            response = http_client.HttpClient.request(method="post", _url=urls.refund_payment_url(self.instance_id),
                                                          arguments= arguments, _key= my_key)
            return response
        except Exception as e:
            return e

    def update_payment(self,arguments, my_key = sentinel):
        be.key_error(my_key)
        try:
            response = http_client.HttpClient.request(method="put", _url=urls.update_payment_url(self.instance_id),
                                                          arguments=arguments, _key=my_key)
            return response
        except Exception as e:
            return e

    @staticmethod
    def list_payments(my_key = sentinel):
        be.key_error(my_key)
        try:
            response = http_client.HttpClient.request(method="get", _url=urls.list_payments_url(), _key=my_key)
            return response
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

# print(Payment.create_payment(arguments={
#     "amount":600,
#     "currency": "SAR",
#     "source":
#         {
#             "type": "creditcard",
#             "name": "Nuha Nasser",
#             "number": "4239399393712333",
#             "cvc": 990,
#             "month": 1,
#             "year": 2022
#         },
#     "callback_url": "https://example.com"
# }
# ))

# p = Payment('5adb88d4-14b3-46bc-a197-30f2e786c976')
# print(p.refund_payment(arguments={"amount": 400}))

# p = Payment('c4b49d02-d3ca-4946-841a-bc0e8ea462f9')
# print(p.fetch_payment())
my_key = Moyasar.test_secret_key('sk_test_DUtsJkXP9hdJYyG4dVTdevz9R5QzbCDrF3KTPDNV')

p = Payment('5adb88d4-14b3-46bc-a197-30f2e786c976')
# print(p.update_payment(arguments={"description": "yay2"}, my_key=my_key))
#

# print(Payment.list_payments(my_key))

print(http_client.__doc__)