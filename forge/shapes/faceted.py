__author__ = 'Nycidian'


class Faceted(object):

    def __init__(self):
        self.shape = 'Faceted'

    def _get_versions_(self):
        versions = []
        this_len = len(self._entries_)

        for i in range(this_len):
            versions.append(self._entries_[i])

        return versions

    def _get_hash_versions_(self):
        versions = []
        this_len = len(self._entries_)
        for i in range(this_len):
            this = []
            for n in range(this_len):

                this.append(self._entries_[((n - i) % this_len)])

            versions.append(tuple(this))

        return versions