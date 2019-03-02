import os
import json
import pytest
import tests.server_stubs as ss
import moyasar


@pytest.fixture
def rootdir():
    return os.path.dirname(os.path.abspath(__file__))


def test_create_should_return_intiated_invoice_for_sadad_source(rootdir):
    params = {"amount": 1000, "currency": "SAR", "description": "Test"}
    ss.stub_server_request("post", moyasar.Invoice.create_url(),
                           resource=os.path.join(rootdir, '../fixtures/invoice.json'), status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    invoice = moyasar.Invoice.create(params)
    assert isinstance(invoice, moyasar.Invoice)
    assert invoice.status == "initiated"
    assert int(invoice.amount) == params['amount']
    assert invoice.currency == params['currency']
    assert invoice.description == params['description']


def test_list_should_return_list_of_invoice_objects(rootdir):
    ss.stub_server_request("get", moyasar.Invoice.list_url(),
                           resource=os.path.join(rootdir, '../fixtures/invoices.json'), status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    invoices = moyasar.Invoice.list()
    assert type(invoices) == list
    assert isinstance(invoices[0], moyasar.Invoice)


def test_find_should_return_invoice_object_if_id_is_correct(rootdir):
    id = '1b82356d-b5fd-46f8-bde9-3680d62f289a'
    ss.stub_server_request("get", moyasar.Invoice.fetch_url(id),
                           resource=os.path.join(rootdir, '../fixtures/invoice.json'), status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    invoice = moyasar.Invoice.fetch(id)
    assert id == invoice.id


def test_update_should_update_invoice_description(rootdir):
    # fetch to update
    id = '1b82356d-b5fd-46f8-bde9-3680d62f289a'
    ss.stub_server_request("get",  moyasar.Invoice.fetch_url(id),
                           resource=os.path.join(rootdir, '../fixtures/invoice.json'), status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    invoice = moyasar.Invoice.fetch(id)
    # update fetched invoice
    ss.stub_server_request("put", f'{moyasar.api_url}/invoices/{invoice.id}',
                           resource=os.path.join(rootdir, '../fixtures/invoice.json'), status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    new_description = {"description": "Test"}
    updated = invoice.update(new_description)
    # simulate updated record
    ss.stub_server_request("post", moyasar.Invoice.create_url(),
                          resource=os.path.join(rootdir, '../fixtures/invoice.json'), status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    after_updated = moyasar.Invoice.create(new_description)

    assert updated.status_code == 200
    # assert new_description["description"] == after_updated.description


def test_cancel_should_return_invoice_object_if_id_is_correct(rootdir):
    id = '1b92356d-b5fd-46f8-bde9-3680d62f289a'
    ss.stub_server_request("get",  moyasar.Invoice.fetch_url(id),
                           resource=os.path.join(rootdir, '../fixtures/invoice.json'), status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    invoice = moyasar.Invoice.fetch(id)
    ss.stub_server_request("put", f'{moyasar.api_url}/invoices/{invoice.id}/cancel',
                           resource=os.path.join(rootdir, '../fixtures/invoice.json'), status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    canceled = invoice.cancel()
    assert canceled.status_code == 200
    assert isinstance(canceled, moyasar.Invoice.__class__)

# test_eqaulity_check_holds_among_identical_invoices_only
# test_eqaulity_check_differentiate_non_identical_invoices
