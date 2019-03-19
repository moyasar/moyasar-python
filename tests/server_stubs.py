import json

import httpretty

API_URI = r"api(mig)?\.moyasar\.com\/v1\/.*"


def stub_server_request(method, url, resource, status=200, error_message= None, errors= None):
    response = ''
    prepare_json = json.dumps(resource)
    if status in range(200, 201):
        response = json.loads(prepare_json)
    elif status in range(400, 429):
        response = {"type": "authentication_error", "message": "Invalid authorization credentials", "errors": None, "http_code": status}
        if status == 401:
            response.update({"type": "authentication_error"})
        if status == 400:
            response.update({"type": "invalid_request_error", "message": error_message, "errors": errors})

    httpretty.enable()
    httpretty.reset()
    httpretty.register_uri(method.upper(), url, body=json.dumps(response), status=status)


def remove_stub():
    httpretty.disable()
