import requests
import json
from moyasar.payment import Payment
from moyasar.invoice import Invoice

api_key = ''
api_version = 'v1'
api_url = f'https://api.moyasar.com/{api_version}'


def resource_url(resource_name):
    return f'{api_url}/{resource_name}s'


def fill_object(object, data):
    for key in data:
        object.__setattr__(key, data[key])


def request(http_verb, url, data):
    request = {
        'method': http_verb.upper(),
        'url': url,
        'auth': (api_key, ''),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
    if data is not None:
        if http_verb.upper() == 'GET':
            request['params'] = data
        else:
            request['data'] = json.dumps(data)

    res = requests.request(**request)
    if res.status_code in range(400, 404):
        json_string = res.text
        json_dict = json.loads(json_string)
        json_dict["http_code"] = res.status_code
        raise Exception(f'{json.dumps(json_dict)}')
    if res.status_code in range(500, 504):
        raise Exception(f'API Error with status code: {res.status_code}')
    return res.text
