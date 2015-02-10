__author__ = 'Nycidian'


class Cast(object):
    """
    Creates the most basic shape for our container
    """

    def __init__(self):
        self._len_value_ = None
        self._hash_value_ = None
        self._versions_ = None

        self.shift = 0

    def __len__(self):
        """
        Checks if length has been computed and stored in _len_value_
            if not does so with a custom function if it exists.
        Returns that stored len.
        """
        if self._len_value_ is None:
            try:
                self._len_value_ = self._len_()
            except AttributeError:
                self._len_value_ = len(self._entries_)

        return self._len_value_

    def _make_versions_(self):
        """
        Checks if _versions_ has been computed
            if not does so with a custom function if it exists or stores default.
        """
        if self._versions_ is None:

            self._versions_ = [self._entries_]

            try:
                self._versions_ = self._get_versions_()
            except AttributeError:
                pass

    def _make_hash_(self):

        this = []
        for version in self._versions_:
            this.append(hash(version))

        return hash(self.__class__.__name__ + str(max(this)))

    def __hash__(self):
        """
        Checks if hash has been computed and stored in _hash_value_
            if not stores default hash.
        Returns that stored hash.
        """
        if self._hash_value_ is None:
                self._hash_value_ = self._make_hash_()

        return self._hash_value_

    def __eq__(self, other):
        try:
            return hash(self) == hash(other)
        except TypeError:
            return False

    def __getitem__(self, key):
        """
        Gets possible values at that place
        """
        # TODO Implement
        pass

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

    def __lshift__(self, other):
        """
        <<  shift left
        :param other: int to shift
        :return: self shifted
        """
        print(other)
        self.shift -= int(other)
        return self

    def __rshift__(self, other):
        """
        >>  shift right
        :param other: int to shift
        :return: self shifted
        """
        print(other)
        self.shift += int(other)
        return self