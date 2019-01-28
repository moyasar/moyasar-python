"""This is the url module.
This module contains global variables payments_url and invoice_url,
 and a set of methods that return well structured Moyasar endpoints.
 The methods are:
 create_payment_url(), fetch_payment_url(payment_id), refund_payment_url(payment_id),
 update_payment_url(payment_id), list_payments_url(),
 create_invoice_url(), fetch_invoice_url(invoice_id), update_invoice_url(invoice_id),
 cancel_invoice_url(invoice_id), list_invoices_url()
"""

payments_url = 'https://api.moyasar.com/v1/payments'
invoice_url = 'https://api.moyasar.com/v1/invoices'

def create_payment_url():
    return payments_url

def fetch_payment_url(payment_id):
    return payments_url+'/'+payment_id

def refund_payment_url(payment_id):
    return payments_url+'/'+payment_id+'/refund'

def update_payment_url(payment_id):
    return payments_url+'/'+payment_id

def list_payments_url():
    return payments_url

def create_invoice_url():
    return invoice_url

def fetch_invoice_url(invoice_id):
    return invoice_url+'/'+invoice_id

def update_invoice_url(invoice_id):
    return invoice_url+'/'+invoice_id

def cancel_invoice_url(invoice_id):
    return invoice_url+'/'+invoice_id+'/cancel'

def list_invoices_url():
    return invoice_url