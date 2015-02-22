__author__ = 'Nycidian'


class Enclosure(object):

    def __init__(self):
        self.shape = 'Enclosure'

    """
    def _get_versions_(self):
        versions = []
        this_len = len(self._entries_)
        for i in range(this_len):
            this = []
            for n in range(this_len):

                this.append(self._entries_[((n - i) % this_len)])

            yield tuple(this)

        raise StopIteration

    """