import moyasar
import tests.fixtures.fixtures as f
import tests.server_stubs as ss


def test_that_it_has_a_version_number():
    assert moyasar.api_version is not ''


def test_should_accept_api_key():
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    assert moyasar.api_key is not ''


def test_request_should_return_json_object():
    ss.stub_server_request(method='GET', url=moyasar.api_url + '/payments',
                           resource=f.payments, status=200)
    response = moyasar.request('GET', moyasar.api_url + '/payments', None)
    assert isinstance(response.json(), dict)
