"""This is the payment module.

This module contains a payment class to accomplish the Moyasar payment service.
"""
# TODO: make parameters shared between invoice and payment
from http_ import http_client
from http_ import urls
from moyasar import Moyasar

class Invoice(Moyasar):

    def __init__(self, instance_id ):
        self.instance_id = instance_id

    @staticmethod
    def create_invoice(arguments, my_key):
        try:
            response = http_client.HttpClient.request(method= "post", _url= urls.create_invoice_url(), arguments=arguments, _key= my_key)
            return response
        except Exception as e:
            print(e)

    def fetch_invoice(self, my_key):
        try:
            response = http_client.HttpClient.request(method= "get", _url= urls.fetch_invoice_url(self.instance_id), _key= my_key)
            return response
        except Exception as e:
            print(e)

    def update_invoice(self, arguments, my_key):
        try:
            response = http_client.HttpClient.request(method="put", _url=urls.update_invoice_url(self.instance_id),
                                                      arguments= arguments, _key= my_key)
            return response
        except Exception as e:
            return e

    def cancel_invoice(self, my_key):
        try:
            response = http_client.HttpClient.request(method="put", _url=urls.cancel_invoice_url(self.instance_id),
                                                      _key= my_key)
            return response
        except Exception as e:
            return e

    @staticmethod
    def list_invoices(my_key):
        try:
            response = http_client.HttpClient.request(method="get", _url=urls.list_invoices_url(),
                                                      _key=my_key)
            return response
        except Exception as e:
            return e

my_key = Moyasar.test_secret_key('sm_test_DUtsJkXP9hdJYyG4dVTdevz9R5QzbCDrF3KTPDNV')
# print(Invoice.create_invoice({
#     "amount":600,
#     "currency": "SAR",
#     "description": "tmp"
# }, my_key))


i = Invoice('388773cf-a39a-4706-8a30-6e56611e942f')

# print(Invoice.fetch_invoice(i,my_key))

# print(i.update_invoice(arguments= {"currency":"SAR"}, my_key=my_key))

print(Invoice.list_invoices(my_key))