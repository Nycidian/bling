__author__ = 'Nycidian'

from congruence import Congruence
congruence_hash = Congruence().make_congruence_set


class Iterable(object):
    """
    Accesses and compares items as an iterable
    """

    def __init__(self, *items):
        self._entries_ = items

        self._versions_ = None
        self._hash_object_ = None

        self.cyclic = False
        self.reflect = False

        self.foundation = 'Iterable'

    def make_iterable(self):
        self._make_hash_()
        self._make_versions_()

    def _make_versions_(self):

        if self._versions_ is None:
            self._versions_ = self._get_versions_

        """
        if self._hash_versions_ is None:

            try:
                self._hash_versions_ = self._get_hash_versions_()
            except AttributeError:
                self._hash_versions_ = self._versions_
        """

    def _make_hash_(self):

        self._hash_object_ = tuple([self.shape, congruence_hash(self._entries_, cyclic=self.cyclic, reflect=self.reflect)])

    def __hash__(self):
        """
        Checks if hash has been computed and stored in _hash_object_
            if not stores default hash.
        Returns that stored hash.
        """

        return hash(self._hash_object_)

    def __eq__(self, other):

        try:
            return self._hash_object_ == other._hash_object_
        except AttributeError:
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

            for version in self._versions_():

                for index in range(len(version)):
                    this = None
                    try:
                        this = version[index].front_of(fragment)
                    except AttributeError:
                        if version[index] == fragment[0]:
                            this = fragment[1:]

                    if this:
                        truth = True
                        fragment = this
                    else:
                        truth = False
                        break

                if truth:
                    return place

        return None

    def front_of(self, other):

        for version in self._versions_():
            truth = True
            fragment = other

            for index in range(len(version)):

                this = None
                try:
                    this = version[index].front_of(fragment)
                except AttributeError:
                    if version[index] == fragment[0]:
                        this = fragment[1:]

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