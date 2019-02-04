"""This is the payment module.
This module contains Payment class that inherits Moyasar class.
Payment class contains static and instance methods to perform moyasar operations,
and these methods are:
create_payment(arguments, my_key), fetch_payment(self, my_key), refund_payment(self, arguments, my_key),
update_payment(self,arguments, my_key), list_payments(my_key)
"""

from moyasar.http_ import urls, http_client
from moyasar._moyasar import Moyasar
from moyasar.errors import BuiltInExceptions as be
from moyasar.globals import sentinel


def create_payment(arguments, my_key=sentinel):
    be.key_unavailability(my_key)
    try:
        response = http_client.HttpClient.request(method="post", _url=urls.create_payment_url(),
                                                  arguments=arguments, _key=my_key)
        return response
    except Exception as e:
        return e



def list_payments(my_key= sentinel):
    be.key_unavailability(my_key)
    try:
        response = http_client.HttpClient.request(method="get", _url= urls.list_payments_url(),
                                                      _key= my_key)
        return response
    except Exception as e:
        return e


class Payment(Moyasar):

    def __init__(self,**kwargs):
        self.id = kwargs['id'] if 'id' in kwargs else None

    def fetch_payment(self, my_key= sentinel):
        be.key_unavailability(my_key)
        try:
            response = http_client.HttpClient.request(method="get", _url= urls.fetch_payment_url(self.id),
                                                      _key= my_key)
            return response
        except Exception as e:
            return e

    def refund_payment(self, arguments, my_key= sentinel):
        be.key_unavailability(my_key)
        try:
            response = http_client.HttpClient.request(method="post", _url= urls.refund_payment_url(self.id),
                                                      arguments= arguments, _key= my_key)
            return response
        except Exception as e:
            return e

    def update_payment(self,arguments, my_key= sentinel):
        be.key_unavailability(my_key)
        try:
            response = http_client.HttpClient.request(method="put", _url= urls.update_payment_url(self.id),
                                                      arguments= arguments, _key= my_key)
            return response
        except Exception as e:
            return e
