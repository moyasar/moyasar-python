"""This module is errors module.
errors module contains two classes inherit from Exception.
The first is APIError which is used to raise API error to the user
in case of 500-504 errors.
The second is BuiltInExceptions class. It contains a static method key_unavailability(my_key),
which validates the presence of user key then raises ValueError exception accordingly, and a static method
invalid_key(msg) which raises a value error when key is invalid
"""

import globals


class APIError(Exception):
    pass


class BuiltInExceptions(Exception):

    @staticmethod
    def key_unavailability(my_key):
        if my_key is globals.sentinel:
            raise ValueError("You did not provide a key")

        elif my_key is None:
            raise ValueError("Your key cannot be None")

        else:
            return

    @staticmethod
    def invalid_key(msg):
        raise ValueError(msg)

