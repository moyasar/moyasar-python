"""This is the http client module.

This module is an http client to provide basic http requests.
"""

import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException
import http_.urls as url

import json

from moyasar import Moyasar


class HttpClient:

    HEADERS = {"content-type": "application/json"}


    @staticmethod
    def request(method, _url= None, arguments= None, _key = None):

        if method is "get" or method is "GET":
            try:
                moyasar_call = requests.get(_url,auth=HTTPBasicAuth(_key,''), headers= HttpClient.HEADERS)
                return moyasar_call.json()
            except RequestException as e:
                print(e)

        if method is "put" or method is "PUT":
            try:
                moyasar_call = requests.put( _url, auth= HTTPBasicAuth(_key,''), json= arguments,
                                            headers= HttpClient.HEADERS )

                if moyasar_call.content is b'':
                    return moyasar_call.status_code
                else:
                    return moyasar_call.json()

            except RequestException as e:
                return e

        if method is "post" or method is "POST":
            try:
                moyasar_call = requests.post(_url,auth= HTTPBasicAuth(_key,''), json= arguments
                                             , headers=HttpClient.HEADERS)
                return moyasar_call.json()
            except RequestException as e:
                return e