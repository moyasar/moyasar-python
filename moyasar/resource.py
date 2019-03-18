from moyasar.actions.fetch import Fetch
from moyasar.actions.list import List
from moyasar.actions.update import Update


class Resource(Fetch, List, Update):
    pass