__author__ = 'Nycidian'

from forge.tool.cast import Cast
from forge.shapes.band import Band


class Ring(Cast, Band):

    def __init__(self, *items):
        Cast.__init__(self)
        Band.__init__(self)

        self._entries_ = items
        self._make_versions_()

