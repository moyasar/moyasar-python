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
        be.key_unavailability(my_key)
        try:
            response = http_client.HttpClient.request(method="post", _url=urls.create_payment_url(), arguments=arguments, _key= my_key)
            return response
        except Exception as e:
            return e



    def fetch_payment(self, my_key = sentinel):
        be.key_unavailability(my_key)
        try:
            response = http_client.HttpClient.request(method="get", _url= urls.fetch_payment_url(self.instance_id), _key= my_key)
            return response
        except Exception as e:
            return e

    def refund_payment(self, arguments, my_key = sentinel):
        be.key_unavailability(my_key)
        try:
            response = http_client.HttpClient.request(method="post", _url=urls.refund_payment_url(self.instance_id),
                                                          arguments= arguments, _key= my_key)
            return response
        except Exception as e:
            return e

    def update_payment(self,arguments, my_key = sentinel):
        be.key_unavailability(my_key)
        try:
            response = http_client.HttpClient.request(method="put", _url=urls.update_payment_url(self.instance_id),
                                                          arguments=arguments, _key=my_key)
            return response
        except Exception as e:
            return e

    @staticmethod
    def list_payments(my_key = sentinel):
        be.key_unavailability(my_key)
        try:
            response = http_client.HttpClient.request(method="get", _url=urls.list_payments_url(), _key=my_key)
            return response
        except Exception as e:
            return e
