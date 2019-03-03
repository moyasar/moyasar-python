import os
import py
import pytest
import moyasar
import tests.server_stubs as ss
import tests.test_helper as th
import json
import tests.fixtures.fixtures as f


def test_that_it_has_a_version_number():
    assert moyasar.api_version is not ''


def test_should_accept_api_key():
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    assert moyasar.api_key is not ''


# def test_request_should_throw_exception_if_key_is_nil():
#     ss.stub_server_request(method='GET', url=moyasar.api_url + '/payments',
#                            resource=f.payments, status=401)
#     moyasar.api_key = ''
#     with pytest.raises(Exception):
#         moyasar.request('GET', moyasar.api_url + '/payments', None)
#
#
# def test_request_return_success_when_correct_key_given():
#     ss.stub_server_request(method='GET', url=moyasar.api_url + '/payments',
#                            resource=f.payments)
#     moyasar.api_key = ''
#     response = moyasar.request('GET', moyasar.api_url + '/payments', None)
#     assert response.status_code == 200


def test_request_should_return_json_object():
    ss.stub_server_request(method='GET', url=moyasar.api_url + '/payments',
                           resource=f.payments, status=200)
    response = moyasar.request('GET', moyasar.api_url + '/payments', None)
    assert isinstance(response.json(), dict)
