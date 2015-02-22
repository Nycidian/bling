__author__ = 'Nycidian'


class Rod(object):
    """
    Default Shape
    """
    def __init__(self):
        self.shape = 'Rod'

    def _get_versions_(self):

        yield tuple(self._entries_)

        raise StopIteration