"""This is Moyasar module.

This module contains credentials needed to use Moyasar services
"""

class Moyasar:

    @staticmethod
    def test_secret_key( _key = None ):
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