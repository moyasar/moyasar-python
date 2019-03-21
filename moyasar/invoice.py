from moyasar.actions.create import Create
from moyasar.resource import Resource
from moyasar.actions.cancel import Cancel
from moyasar.helpers import Format


class Invoice(Resource, Cancel, Create, Format):
    pass
