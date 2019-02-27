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


def stub_server_request(resource, key, status=200, body={},
                        error_message=None, errors=None):
    response = ''

    if status in range(200, 201):
        resource = json.loads(open(resource).read())
        return resource

    if status in range(400, 429):
        defaults = {"type": "authentication_error", "message": "Invalid authorization credentials", "errors": None, "http_code": status}
        if status == 401:
            defaults.update({"type": "authentication_error", "http_code": 401})
            response = defaults
            # raise Exception(f'{json.dumps(response)}')
        if status == 400:
            defaults.update({"type": "invalid_request_error", "http_code": 400})
            response = defaults
            return response

    string = '%s:%s' % (f'{key}', '')
    base64string = base64.standard_b64encode(string.encode('utf-8'))

    httpretty.register_uri(httpretty.OPTIONS, API_URI,
                           adding_headers={"Authorization": "Basic %s" % base64string.decode('utf-8')},
                           body=response)

    # adapter = requests_mock.Adapter()
    # adapter.register_uri(requests_mock.ANY, API_URI, request_headers=
    # {"Authorization": "Basic %s" % base64string.decode('utf-8')}, json=response, status_code=status)
