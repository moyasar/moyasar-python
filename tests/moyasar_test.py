import os
import py
import pytest
import moyasar
import tests.server_stubs as ss
import tests.test_helper as th
import json


@pytest.fixture
def rootdir():
    return os.path.dirname(os.path.abspath(__file__))


def test_that_it_has_a_version_number():
    assert moyasar.api_version is not ''


def test_should_accept_api_key():
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    assert moyasar.api_key is not ''


def test_request_should_throw_exception_if_key_is_nil(rootdir):
    ss.stub_server_request(method='GET', url=moyasar.api_url + '/payments',
                           resource=os.path.join(rootdir, 'fixtures/payments.json'), status=401)
    with pytest.raises(Exception):
        moyasar.request('GET', moyasar.api_url + '/payments', None)


# def test_request_should_read_api_key_class_variable_if_key_not_given(rootdir):
#     ss.stub_server_request(method='GET', url=moyasar.api_url + '/payments', resource=os.path.join(rootdir, 'fixtures/payments.json'))
#     moyasar.api_key = th.TEST_KEY
#     response = moyasar.request('GET', moyasar.api_url + '/payments', None)
#     assert response.status_code == 200


# def test_request_should_raise_authentication_error_when_use_wrong_api_key(rootdir):
#     ss.stub_server_request(method='GET', url=moyasar.api_url + '/payments', resource=os.path.join(rootdir, 'fixtures/payments.json'), status=401)
#     moyasar.api_key = 'WrongKey'
#     with pytest.raises(Exception):
#         moyasar.request('GET', moyasar.api_url + '/payments', None)


def test_request_return_success_when_correct_key_given(rootdir):
    ss.stub_server_request(
        method='GET',
        url=moyasar.api_url + '/payments',
        resource=os.path.join(rootdir, 'fixtures/payments.json'),
        status=200
    )

    response = moyasar.request('GET', moyasar.api_url + '/payments', None)
    assert response.status_code == 200


def test_request_should_return_json_object():
    pass
