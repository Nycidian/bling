__author__ = 'Nycidian'

from forge.tool.cast import Cast
from forge.shapes.faceted import Faceted


class Gem(Cast, Faceted):

    def __init__(self, *items):
        Cast.__init__(self)
        Faceted.__init__(self)

        self._entries_ = items
        self._make_versions_()


