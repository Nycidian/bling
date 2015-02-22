__author__ = 'Nycidian'

from forge.foundations.iterable import Iterable
from forge.shapes.rod import Rod


class Chain(Iterable, Rod):

    def __init__(self, *items):
        Iterable.__init__(self, *items)
        Rod.__init__(self)

        self.make_iterable()