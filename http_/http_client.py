"""This is the http client module.

This module is an http client to provide basic http requests.
"""

import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException
import http_.urls as url

import json
from errors import APIError
from moyasar import Moyasar


class HttpClient:
# TODO: parse http
    HEADERS = {"content-type": "application/json"}

    @staticmethod
    def request(method, _url= None, arguments= None, _key = None):

        if method is "get" or method is "GET":
            try:
                response = requests.get(_url,auth=HTTPBasicAuth(_key,''), headers= HttpClient.HEADERS)
                response_body = response.json()
                http_code = response.status_code
                return HttpClient.handle_response(http_code, response_body)
            except RequestException as e:
                return e

        if method is "put" or method is "PUT":
            try:
                response = requests.put( _url, auth= HTTPBasicAuth(_key,''), json= arguments,
                                            headers= HttpClient.HEADERS )

                if response.content is b'':
                    # does not return moyasar object, only a status code
                    # ex. PUT https://api.moyasar.com/v1/payments/:id
                    return response.status_code
                else:
                    response_body = response.json()
                    http_code = response.status_code
                    return HttpClient.handle_response(http_code, response_body)

            except RequestException as e:
                return e

        if method is "post" or method is "POST":
            try:
                response = requests.post(_url,auth= HTTPBasicAuth(_key,''), json= arguments
                                             , headers=HttpClient.HEADERS)
                response_body = response.json()
                http_code = response.status_code
                return HttpClient.handle_response(http_code, response_body)
            except RequestException as e:
                return e

    @staticmethod
    def handle_response(http_code, response_body = None):
        if http_code in range(400,429,1):
            response_body["http_code"] = http_code
            return response_body
        elif http_code in range(500,504,1):
            raise APIError('We had a problem with Moyasar server')
        else: # 200
            return response_body