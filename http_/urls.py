"""This is the url module.

This module returns the full path to Moyasar endpoints
"""

payments_url = 'https://api.moyasar.com/v1/payments'

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

