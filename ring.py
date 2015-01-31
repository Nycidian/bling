__author__ = 'Nycidian'

import math
import inspect
import itertools


class Ring(object):

    def __init__(self, *items):
        self._items = tuple(items)

        self._hash_ = self._make_hash_()

    def _make_hash_(self):
        this = []
        for i in range(len(self._items)):
                string = ''
                for n in range(len(self._items)):
                    string += str(hash(self._items[((n - i) % len(self._items))]))
                this.append(string)
        print(max(this))
        return hash(max(this))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return self._hash_

    def __str__(self):

        return str(self._items)

    def __repr__(self):
        return str(self._items)

    @staticmethod
    def __bool__():
        return True

    def __nonzero__(self):      # Python 2 compatibility
        return type(self).__bool__(self)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, key):
        """
        Modular Retrieval
        """
        return self._items[(key % len(self))]

    def __setitem__(self, key, point):
        # TODO Raise Error
        pass

    def __iter__(self):
        # TODO Add indefinite cyclical iteration
        pass

    def __contains__(self, item):
        # TODO add function that checks if a single object is in or if a tuple of objects is contained within in order
        pass

if __name__ == '__main__':
    pass
