__author__ = 'Nycidian'


class Band(object):
    """
    Cyclic
    """
    def __init__(self):
        self.shape = 'Band'

    def _get_versions_(self):
        versions = []
        this_len = len(self._entries_)
        for i in range(this_len):
            this = []
            for n in range(this_len):

                this.append(self._entries_[((n - i) % this_len)])

            versions.append(tuple(this))

        return versions
