"""This is the invoice module.
This module contains Invoice class that inherits Moyasar class.
Invoice class contains static and instance methods to perform moyasar operations,
and these methods are:
create_invoice(arguments, my_key), fetch_invoice(self, my_key), update_invoice(self, arguments, my_key),
list_invoices(my_key).
"""

from moyasar.http_ import urls, http_client
from moyasar._moyasar import Moyasar
from moyasar.globals import sentinel
from moyasar.errors import BuiltInExceptions as be


class Invoice(Moyasar):


    def __init__(self, instance_id):
        self.instance_id = instance_id


    @staticmethod
    def create_invoice(arguments, my_key= sentinel):

        be.key_unavailability(my_key)

        try:
            response = http_client.HttpClient.request(method="post", _url= urls.create_invoice_url(),
                                                      arguments= arguments, _key= my_key)
            return response
        except Exception as e:
            print(e)

    def fetch_invoice(self, my_key= sentinel):

        be.key_unavailability(my_key)

        try:
            response = http_client.HttpClient.request(method="get", _url= urls.fetch_invoice_url(self.instance_id),
                                                      _key= my_key)
            return response
        except Exception as e:
            print(e)

    def update_invoice(self, arguments, my_key= sentinel):

        be.key_unavailability(my_key)

        try:
            response = http_client.HttpClient.request(method="put", _url= urls.update_invoice_url(self.instance_id),
                                                      arguments= arguments, _key= my_key)
            return response
        except Exception as e:
            return e

    def cancel_invoice(self, my_key= sentinel):

        be.key_unavailability(my_key)

        try:
            response = http_client.HttpClient.request(method="put", _url= urls.cancel_invoice_url(self.instance_id),
                                                      _key= my_key)
            return response
        except Exception as e:
            return e

    @staticmethod
    def list_invoices(my_key= sentinel):

        be.key_unavailability(my_key)

        try:
            response = http_client.HttpClient.request(method="get", _url= urls.list_invoices_url(),
                                                      _key= my_key)
            return response
        except Exception as e:
            return e

