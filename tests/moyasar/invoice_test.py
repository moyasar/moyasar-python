import copy

import moyasar
import tests.fixtures.fixtures as f
import tests.server_stubs as ss


def test_create_should_return_intiated_invoice_for_sadad_source():
    params = {"amount": 1000, "currency": "SAR", "description": "Test"}
    ss.stub_server_request("post", moyasar.Invoice.create_url(),
                           resource=f.invoice, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    invoice = moyasar.Invoice.create(params)
    assert isinstance(invoice, moyasar.Invoice)
    assert invoice.status == "initiated"
    assert int(invoice.amount) == params['amount']
    assert invoice.currency == params['currency']
    assert invoice.description == params['description']


def test_list_should_return_list_of_invoice_objects():
    ss.stub_server_request("get", moyasar.Invoice.list_url(),
                           resource=f.invoices, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    invoices = moyasar.Invoice.list()
    assert type(invoices) == list
    assert isinstance(invoices[0], moyasar.Invoice)


def test_find_should_return_invoice_object_if_id_is_correct():
    id = '1b82356d-b5fd-46f8-bde9-3680d62f289a'
    ss.stub_server_request("get", moyasar.Invoice.fetch_url(id),
                           resource=f.invoice, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    invoice = moyasar.Invoice.fetch(id)
    assert invoice.id == id


def test_update_should_update_invoice_description():
    # fetch to update
    id = '1b82356d-b5fd-46f8-bde9-3680d62f289a'
    ss.stub_server_request("get",  moyasar.Invoice.fetch_url(id),
                           resource=f.invoice, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    invoice = moyasar.Invoice.fetch(id)
    # update fetched invoice
    ss.stub_server_request("put", f'{moyasar.api_url}/invoices/{invoice.id}',
                           resource=f.invoice, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    new_description = {"description": "Test"}
    updated = invoice.update(new_description)
    # simulate updated record
    ss.stub_server_request("post", moyasar.Invoice.create_url(),
                          resource=f.invoice, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    after_updated = moyasar.Invoice.create(new_description)

    assert updated.status_code == 200
    assert new_description["description"] == after_updated.description


def test_cancel_should_return_invoice_object_if_id_is_correct():
    # copy resource to prepare a custom version for this case
    cancel_resource = copy.deepcopy(f.invoice)
    cancel_resource.update({"status": "canceled"})
    id = '1b92356d-b5fd-46f8-bde9-3680d62f289a'
    ss.stub_server_request("get",  moyasar.Invoice.fetch_url(id),
                           resource=cancel_resource, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    invoice = moyasar.Invoice.fetch(id)
    ss.stub_server_request("put", f'{moyasar.api_url}/invoices/{invoice.id}/cancel',
                           resource=cancel_resource, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    canceled = invoice.cancel()
    assert canceled["status"] == "canceled"


def test_eqaulity_check_holds_among_identical_invoices_only():
    id = '1b82356d-b5fd-46f8-bde9-3680d62f289a'
    ss.stub_server_request("get",  moyasar.Invoice.fetch_url(id),
                           resource=f.invoice, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    invoice_one = moyasar.Invoice.fetch(id)
    ss.remove_stub()
    ss.stub_server_request("get",  moyasar.Invoice.fetch_url(id),
                           resource=f.invoice, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    invoice_two = moyasar.Invoice.fetch(id)
    invoice_one_values = []
    for val in invoice_one.__dict__.values():
        invoice_one_values.append(val)
    invoice_two_values = []
    for val in invoice_two.__dict__.values():
        invoice_two_values.append(val)
    assert invoice_one_values == invoice_two_values


def test_eqaulity_check_differentiate_non_identical_invoices():
    id = '1b82356d-b5fd-46f8-bde9-3680d62f289a'
    ss.stub_server_request("get", moyasar.Invoice.fetch_url(id),
                           resource=f.invoice, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    invoice_one = moyasar.Invoice.fetch(id)
    ss.remove_stub()
    modified_resource = copy.deepcopy(f.invoice)
    modified_resource.update({"amount": "5000"})
    ss.stub_server_request("get", moyasar.Invoice.fetch_url(id),
                           resource=modified_resource, status=200)
    moyasar.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
    invoice_two = moyasar.Invoice.fetch(id)
    invoice_one_values = []
    for val in invoice_one.__dict__.values():
        invoice_one_values.append(val)
    invoice_two_values = []
    for val in invoice_two.__dict__.values():
        invoice_two_values.append(val)
    assert invoice_one_values != invoice_two_values
