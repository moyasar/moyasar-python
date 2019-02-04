"""This is the http client module.
This module contains HttpClient class that contains the following:

HEADER: a const class variable to determine http headers.
request(): a static method to establish http requests regardless of http verbs.
handle_response(): a static method to classify http response status code,
 and handle it according to that.
"""

import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException

from moyasar.errors import APIError
from moyasar.moyasar_ import get_api_key, set_api_key



HEADERS = {"content-type": "application/json"}


def request(method, _url= None, arguments= None, _key= None):
    api_key = get_api_key()
    if method is "get" or method is "GET":
        try:
            response = requests.get(_url, auth= HTTPBasicAuth(api_key,''), headers= HEADERS)
            response_body = response.json()
            http_code = response.status_code
            return handle_response(http_code, response_body)
        except RequestException as e:
            return e

    if method is "put" or method is "PUT":
        try:
            response = requests.put( _url, auth= HTTPBasicAuth(api_key,''), json= arguments,
                                            headers= HEADERS)

            if response.content is b'':
                # Does not return moyasar object, only a status code
                # E.x., PUT https://api.moyasar.com/v1/payments/:id
                return response.status_code
            else:
                response_body = response.json()
                http_code = response.status_code
                return handle_response(http_code, response_body)
        except RequestException as e:
            return e

    if method is "post" or method is "POST":
        try:
            response = requests.post(_url, auth= HTTPBasicAuth(api_key, ''), json= arguments
                                             , headers= HEADERS)
            response_body = response.json()
            http_code = response.status_code
            return handle_response(http_code, response_body)
        except RequestException as e:
            return e



def handle_response(http_code, response_body= None):

    if http_code in range(400,429,1):
        response_body["http_code"] = http_code
        return response_body

    elif http_code in range(500,504,1):
        raise APIError('We had a problem with Moyasar server')

    else:  # In case of 200 status code
        return response_body