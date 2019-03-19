import copy

import moyasar
import tests.fixtures.fixtures as f
import tests.server_stubs as ss


def test_list_should_return_list_of_payment_objects():
    ss.stub_server_request("get", moyasar.Payment.list_url(),
                           resource=f.payments, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    payments = moyasar.Payment.list()
    assert type(payments) == list
    assert isinstance(payments[0], moyasar.Payment)


def test_find_should_return_payemnt_object_if_id_is_correct():
    id = '328f5dca-91ec-435d-b13f-86052a1d0f7b'
    ss.stub_server_request("get", moyasar.Payment.fetch_url(id),
                           resource=f.payment, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    payment = moyasar.Payment.fetch(id)
    assert payment.id == id


def test_update_should_update_payment_description():
    # fetch to update
    id = '328f5dca-91ec-435d-b13f-86052a1d0f7b'
    ss.stub_server_request("get", moyasar.Payment.fetch_url(id),
                           resource=f.payment, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    payment = moyasar.Payment.fetch(id)
    # update fetched payment
    ss.stub_server_request("put", f'{moyasar.api_url}/payments/{payment.id}',
                           resource=f.payment, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    new_description = {"description": "Test"}
    updated = payment.update(new_description)
    # simulate updated record
    ss.stub_server_request("post", moyasar.Payment.create_url(),
                           resource=f.invoice, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    after_updated = moyasar.Payment.create(new_description)

    assert updated.status_code == 200
    assert new_description["description"] == after_updated.description


def test_eqaulity_check_holds_among_identical_payments_only():
    id = '1b82356d-b5fd-46f8-bde9-3680d62f289a'
    ss.stub_server_request("get", moyasar.Payment.fetch_url(id),
                           resource=f.payment, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    payment_one = moyasar.Payment.fetch(id)
    ss.remove_stub()
    ss.stub_server_request("get", moyasar.Payment.fetch_url(id),
                           resource=f.payment, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    payment_two = moyasar.Payment.fetch(id)

    payment_one_values = []
    payment_two_values = []
    for key, val in payment_one.__dict__.items():
        if key != 'source':
            payment_one_values.append(val)
        if key == 'source':
            for k, v in val.__dict__.items():
                payment_one_values.append(v)
    for key, val in payment_two.__dict__.items():
        if key != 'source':
            payment_two_values.append(val)
        if key == 'source':
            for k, v in val.__dict__.items():
                payment_two_values.append(v)
    assert payment_one_values == payment_two_values


def test_eqaulity_check_differentiate_non_identical_payments():
    id = '1b82356d-b5fd-46f8-bde9-3680d62f289a'
    ss.stub_server_request("get", moyasar.Payment.fetch_url(id),
                           resource=f.payment, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    payment_one = moyasar.Payment.fetch(id)
    ss.remove_stub()
    modified_resource = copy.deepcopy(f.payment)
    modified_resource.update({"amount": "5000"})
    ss.stub_server_request("get", moyasar.Payment.fetch_url(id),
                           resource=modified_resource, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    payment_two = moyasar.Payment.fetch(id)

    payment_one_values = []
    payment_two_values = []
    for key, val in payment_one.__dict__.items():
        if key != 'source':
            payment_one_values.append(val)
        if key == 'source':
            for k, v in val.__dict__.items():
                payment_one_values.append(v)
    for key, val in payment_two.__dict__.items():
        if key != 'source':
            payment_two_values.append(val)
        if key == 'source':
            for k, v in val.__dict__.items():
                payment_two_values.append(v)
    assert payment_one_values != payment_two_values