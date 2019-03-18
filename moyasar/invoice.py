from moyasar.actions.create import Create
from moyasar.resource import Resource
from moyasar.actions.cancel import Cancel


class Invoice(Resource, Cancel, Create):
    pass
