__author__ = 'Nycidian'

from math import fabs


class Iterable(object):
    """
    Accesses and compares items as an iterable
    """

    def __init__(self, *items):
        self._entries_ = items
        self._hash_value_ = None
        self._versions_ = None
        self._hash_versions_ = None

        self.foundation = 'Iterable'


    def _make_versions_(self):
        """
        Checks if _versions_ has been computed
            if not does so with a custom function if it exists or stores default.
        """
        if self._versions_ is None:

            try:
                self._versions_ = self._get_versions_()
            except AttributeError:
                self._versions_ = [self._entries_]

        if self._hash_versions_ is None:

            try:
                self._hash_versions_ = self._get_hash_versions_()
            except AttributeError:
                self._hash_versions_ = self._versions_

    def _make_hash_(self):

        this = []
        for version in self._hash_versions_:
            this.append(hash(version))

        self._hash_value_ = str(hash(self.shape)) + str(int(fabs(max(this))))

    def __hash__(self):
        """
        Checks if hash has been computed and stored in _hash_value_
            if not stores default hash.
        Returns that stored hash.
        """

        return int(self._hash_value_)

    def __eq__(self, other):
        try:
            return hash(self) == hash(other)
        except TypeError:
            return False

    def _get_modular_entry_(self, key):
        return key % len(self._entries_)

    @staticmethod
    def __bool__():
        return True

    def __nonzero__(self):      # Python 2 compatibility
        return type(self).__bool__()

    def __str__(self):
        return '{}{}'.format(self.__class__.__name__, self._entries_)

    def __repr__(self):
        return '{}{}'.format(self.__class__.__name__, self._entries_)

    def out_of(self, other):

        for place in range(len(other)):
            truth = False
            fragment = other[place:]

            for version in self._versions_:
                print('out_of version', version)
                print('out_of fragment', fragment)
                for index in range(len(version)):
                    this = None
                    try:
                        this = version[index].front_of(fragment)
                    except AttributeError:
                        if version[index] == fragment[0]:
                            this = fragment[1:]
                    print('out_of this', this)
                    if this:
                        truth = True
                        fragment = this
                    else:
                        truth = False
                        print('out_of break')
                        break

                if truth:
                    return place

        return None

    def front_of(self, other):

        for version in self._versions_:
            truth = True
            fragment = other
            print('front_of version', version)
            print('front_of fragment', fragment)
            for index in range(len(version)):
                print('front_of index', version[index])
                this = None
                try:
                    this = version[index].front_of(fragment)
                except AttributeError:
                    if version[index] == fragment[0]:
                        this = fragment[1:]
                print('front_of this', this)
                if this:
                    fragment = this
                else:
                    truth = False
                    break

            if truth:
                return fragment

        return None

    def back_of(self, other):
        print('back of')