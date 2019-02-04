"""This is the payment module.
This module contains Payment class that inherits Moyasar class.
Payment class contains static and instance methods to perform moyasar operations,
and these methods are:
create_payment(arguments, my_key), fetch_payment(self, my_key), refund_payment(self, arguments, my_key),
update_payment(self,arguments, my_key), list_payments(my_key)
"""

from moyasar.http_ import urls, http_client
from moyasar.errors import sentinel


class CreditCard:
    def __init__(self, type, company, name, number, message, transaction_url):
        self.type = type
        self.company = company
        self.name = name
        self.number = number
        self.message = message
        self.transaction_url = transaction_url
    pass


class Sadad:
    def __init__(self, type, username, error_code, message, transaction_id, transaction_url):
        self.type = type
        self.username = username
        self.error_code = error_code
        self.message = message
        self.transaction_id = transaction_id
        self.transaction_url = transaction_url


def create_payment(arguments, my_key=sentinel):
    try:
        response = http_client.request(method="post", _url=urls.create_payment_url(),
                                                  arguments=arguments, _key=my_key)
        return response
    except Exception as e:
        return e


def list_payments(my_key= sentinel):
    try:
        response = http_client.request(method="get", _url= urls.list_payments_url(),
                                                      _key= my_key)
        return response
    except Exception as e:
        return e


def fetch_payment(id= None):
    try:
        response = http_client.request(method="get", _url=urls.fetch_payment_url(id))
        return obj(response)
    except Exception as e:
        return e

def obj(response):
    payment = response
    sadad = response['source']
    credit_card = response['source']
    payment_object = Payment(
        id=payment['id'],
        status=payment['status'],
        amount=payment['amount'],
        fee=payment['fee'],
        currency=payment['currency'],
        refunded=payment['refunded'],
        refunded_at=payment['refunded_at'],
        description=payment['description'],
        amount_format=payment['amount_format'],
        invoice_id=payment['invoice_id'],
        ip=payment['ip'],
        callback_url=payment['callback_url'],
        created_at=payment['created_at'],
        updated_at=payment['updated_at'],
        source=Sadad(
            type=sadad['type'],
            username=sadad['username'],
            error_code=sadad['error_code'],
            message=sadad['message'],
            transaction_id=sadad['transaction_id'],
            transaction_url=sadad['transaction_url']
        ) if response['source']['type'] is "sadad"
        else CreditCard(
            type=credit_card['type'],
            company=credit_card['company'],
            name=credit_card['name'],
            number=credit_card['number'],
            message=credit_card['message'],
            transaction_url=credit_card['transaction_url']
        )
    )
    return payment_object



class Payment:

    def __init__(self,**kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])


    def update_payment(self, arguments, my_key=sentinel):
        try:
            response = http_client.request(method="put", _url=urls.update_payment_url(self.id),
                                                          arguments=arguments, _key=my_key)
            return response
        except Exception as e:
            return e


    def refund_payment(self, arguments, my_key=sentinel):
        try:
            response = http_client.request(method="post", _url=urls.refund_payment_url(self.id),
                                                          arguments=arguments, _key=my_key)
            return response
        except Exception as e:
            return e


key = set_api_key('sk_test_DUtsJkXP9hdJYyG4dVTdevz9R5QzbCDrF3KTPDNV')
i = fetch_payment('5adb88d4-14b3-46bc-a197-30f2e786c976')
print(i)