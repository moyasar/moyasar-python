"""This is moyasar module.
This module contains class Moyasar that is currently used to validate user provided key,
and to it contains static methods that return keys, a method per Moyasar key (live secret, test publishable..)
allowing moyasar-python lib user to use for example both test secret and test publishable
in more explicit Pythonic manner.
The methods are:
test_secret_key( _key ), test_publishable_key( _key ), live_secret_key( _key ), live_publishable_key( _key )
"""


API_KEY = ''

def set_api_key(key):
    global API_KEY
    API_KEY = key

def get_api_key():
    global API_KEY
    return API_KEY