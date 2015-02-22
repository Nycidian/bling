__author__ = 'Nycidian'

from forge.foundations.temporal import Temporal
from forge.shapes.enclosure import Enclosure


class Clasp(Temporal, Enclosure):

    def __init__(self, before, present, after=None, mirror=False):
        Temporal.__init__(self, before, present, after, mirror)
        Enclosure.__init__(self)

        self._make_versions_()
        self._make_hash_()