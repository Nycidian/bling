__author__ = 'Nycidian'

from forge.tool.cast import Cast
from forge.shapes.bar import Bar


class Chain(Cast, Bar):

    def __init__(self, *items):
        Cast.__init__(self)
        Bar.__init__(self)

        self._entries_ = items
        self._make_versions_()