import moyasar
import tests.server_stubs as ss
import tests.fixtures.fixtures as f
import copy
import pytest


def test_create_should_return_intiated_payment_for_sadad_source():
    params = {"amount": 1000, "currency": "SAR", "description": "Test"}
    ss.stub_server_request("post", moyasar.Payment.create_url(),
                           resource=f.payment, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    payment = moyasar.Payment.create(params)
    assert isinstance(payment, moyasar.Payment)
    assert payment.status == "initiated"
    assert int(payment.amount) == params['amount']
    assert payment.currency == params['currency']
    assert payment.description == params['description']


def test_create_with_amount_less_than_100_cent_should_raise_validation_errror():
    modified_resource = copy.deepcopy(f.payment)
    modified_resource.update({"amount": 90})
    ss.stub_server_request('post', moyasar.Payment.create_url(), resource=modified_resource,
                           status=400, error_message="Validation Failed",
                           errors={"amount": "must be greater than 99"})
    assert pytest.raises(Exception)


def test_create_payment_for_inovice_should_be_acceptable():
    ss.stub_server_request("get", moyasar.Invoice.list_url(),
                           resource=f.invoices, status=200)
    invoices = moyasar.Invoice.list()
    first_invoice_id = ''
    for key, val in invoices[0].__dict__.items():
        if key == "id":
            first_invoice_id = val

    modified_resource = copy.deepcopy(f.payment)
    modified_resource.update({"invoice_id": first_invoice_id})
    ss.stub_server_request("post", moyasar.Payment.create_url(),
                           resource=modified_resource, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    payment = moyasar.Payment.create(modified_resource)
    assert isinstance(payment, moyasar.Payment)
    assert payment.invoice_id == first_invoice_id


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


# def test_refund_should_operate_normally_by_recharging_back_all_amount_as_a_default():
#     id = '328f5dca-91ec-435d-b13f-86052a1d0f7b'
#     ss.stub_server_request("get", moyasar.Payment.fetch_url(id),
#                            resource=f.payment, status=200)
#     moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
#     original = moyasar.Payment.fetch(id)
#     params = {'status': 'refunded', 'refunded': original.amount}
#     custom_invoice = copy.deepcopy(f.payment)
#     custom_invoice.update(params)
#     ss.stub_server_request("post", f'{moyasar.api_url}/payments/{id}/refund',
#                            resource=custom_invoice, status=200)
#     moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
#     refunded = original.refund(amount=original.amount)


def test_refund_should_accept_partial_refund_amounts():
    pass


def test_refund_with_failed_payment_should_raise_invalid_request_error():
    pass


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