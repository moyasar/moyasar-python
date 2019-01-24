"""This is the http client module.

This module is an http client to provide basic http requests.
"""

import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException
import http_.urls as url

import json

from moyasar import Moyasar


class HttpClient(Moyasar):

    _key = Moyasar.test_publishable_key


    @classmethod
    def request(cls,method, _url= None, arguments= None ):

        if method is "get" or method is "GET":
            try:
                moyasar_call = requests.get(_url,auth=HTTPBasicAuth(HttpClient._key,''))
                return moyasar_call.json()
            except RequestException as e:
                print(e)

        if method is "put" or method is "PUT":
            try:
                moyasar_call = requests.put(_url, auth= HTTPBasicAuth(HttpClient._key,''), json= arguments)
                return moyasar_call.json()
            except RequestException as e:
                return e

        if method is "post" or method is "POST":
            try:
                print('here')
                moyasar_call = requests.post(_url,auth= HTTPBasicAuth(HttpClient._key,''),json= arguments)
                print('here2')
                return moyasar_call.json()
            except RequestException as e:
                return e


# h = HttpClient.request("post", _url= url.refund_payment_url('cc3886a6-71b7-477b-9fde-8d11b20a4ecd'),
# key = HttpClient.sk_key ,arguments= {"amount": 100})
# print(h)

# print(HttpClient.request(method= 'get', _url= url.list_payments_url()))