__author__ = 'Nycidian'

from forge.foundations.iterable import Iterable
from forge.shapes.faceted import Faceted


class Gem(Iterable, Faceted):

    def __init__(self, *items):
        Iterable.__init__(self, *items)
        Faceted.__init__(self)

        self.make_iterable()

