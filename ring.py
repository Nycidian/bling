__author__ = 'Nycidian'

from bling.forge.foundations.iterable import Iterable
from bling.forge.shapes.band import Band


class Ring(Iterable, Band):

    def __init__(self, *items):
        Iterable.__init__(self, *items)
        Band.__init__(self)

        self.cyclic = True
        self.make_iterable()

