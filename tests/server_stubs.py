import base64
import os
import pytest
import json
import httpretty

API_URI = r"api(mig)?\.moyasar\.com\/v1\/.*"


# FIXTURE_DIR = os.path.join(
#     os.path.dirname(os.path.realpath(__file__)),
#     'fixtures',
# )
#
#
# @pytest.mark.datafiles(
#     os.path.join(FIXTURE_DIR, 'invoice.json'),
#     os.path.join(FIXTURE_DIR, 'invoices.json'),
#     os.path.join(FIXTURE_DIR, 'payment.json'),
#     os.path.join(FIXTURE_DIR, 'payments.json'),
# )


def stub_server_request(method, url, resource, status=200):
    response = ''
    prepare_json = json.dumps(resource)
    if status in range(200, 201):
        response = json.loads(prepare_json)
    elif status in range(400, 429):
        response = {"type": "authentication_error", "message": "Invalid authorization credentials", "errors": None, "http_code": status}
        if status == 401:
            response.update({"type": "authentication_error", "http_code": 401})
        if status == 400:
            response.update({"type": "invalid_request_error", "http_code": 400})

    httpretty.enable()
    httpretty.reset()
    httpretty.register_uri(method.upper(), url, body=json.dumps(response), status=status)


def remove_stub():
    httpretty.disable()