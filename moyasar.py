"""This is moyasar module.
This module contains class Moyasar that is currently used to validate user provided key,
and to it contains static methods that return keys, a method per Moyasar key (live secret, test publishable..)
allowing moyasar-python lib user to use for example both test secret and test publishable
in more explicit Pythonic manner.
The methods are:
test_secret_key( _key ), test_publishable_key( _key ), live_secret_key( _key ), live_publishable_key( _key )
"""

class Moyasar:

    @staticmethod
    def test_secret_key( _key ):
        if _key.startswith('sk_test'):
            return _key
        else:
            raise ValueError('Invalid Test Secret Key')


    @staticmethod
    def test_publishable_key( _key ):
        if _key.startswith('pk_test'):
            return _key
        else:
            raise ValueError('Invalid Test Publishable Key')

    @staticmethod
    def live_secret_key( _key ):
        if _key.startswith('sk_live'):
            return _key
        else:
            raise ValueError('Invalid Live Secret Key')

    @staticmethod
    def live_publishable_key( _key ):
        if _key.startswith('pk_live'):
            return _key
        else:
            raise ValueError('Invalid Live Publishable Key')