__author__ = 'Nycidian'

# basestring for python 3
try:
    basestring
except NameError:
    basestring = str


class Setting(object):
    """
    Container that evaluates to true if any one of the contents is equal to what it's tested against
    """

    def __init__(self, *items):
        self._items = tuple(items)

    @staticmethod
    def __bool__():
        return True

    def __nonzero__(self):      # Python 2 compatibility
        return type(self).__bool__(self)

    def __hash__(self):
        return hash(self._items)

    def __eq__(self, other):
        truth = False
        for item in self._items:
            truth = truth or (item == other)

        return truth


class Cast(object):

    def __init__(self, *items):
        self._items = tuple(items)

    def __eq__(self, other):
        try:
            return hash(self) == hash(other)
        except TypeError:
            return False

    def __hash__(self):
        this = []
        for i in range(len(self._items)):
            string = self.__class__.__name__
            for n in range(len(self._items)):
                string += str(hash(self._items[n - i]))
            this.append(string)
        return hash(max(this))

    def __getitem__(self, key):
        """
        Modular Retrieval
        """

        return self._items[(key % len(self))]

    def __str__(self):
        return str(self._items)

    def __repr__(self):
        return str(self._items)

    def __len__(self):
        return len(self._items)


class Band(object):

    def __init__(self, *items):
        self.entry = tuple(items)
        self.extrapolated = [tuple(items)]
        self._extrapolate_()
        self._versions_ = self._get_versions_()
        self._hash_ = self._make_hash_()

    def _extrapolate_(self):

        def banded():
            if len(self.extrapolated) == 0:
                return False
            bands = 0
            for item in self.extrapolated:
                for i in item:
                    if isinstance(i, Band):
                        bands += 1
            if bands > 0:
                return True
            return False

        while banded():
            extraps = []
            for line in self.extrapolated:

                for i in range(len(line)):
                    if isinstance(line[i], Band):
                        for version in line[i].versions():
                            extraps.append(tuple(list(line[:i])+list(version)+list(line[i+1:])))
            self.extrapolated = tuple(extraps)

        s = set()
        if self.__class__.__name__ == 'Ring':
            # Ring Class
            for item in self.extrapolated:
                s.add(Cast(*item))
        else:
            for item in self.extrapolated:
                s.add(item)
        self.extrapolated = list(s)


    def _get_versions_(self):
        return self.extrapolated

    def _make_hash_(self):

        this = []
        for version in self._versions_:
            this.append(hash(version))

        return hash(self.__class__.__name__ + str(max(this)))

    def __hash__(self):
        return self._hash_

    def __eq__(self, other):
        try:
            return hash(self) == hash(other)
        except TypeError:
            return False

    def __str__(self):
        return str(self.entry)

    def __repr__(self):
        return str(self.entry)

    @staticmethod
    def __bool__():
        return True

    def __nonzero__(self):      # Python 2 compatibility
        return type(self).__bool__(self)

    def __len__(self):
        return len(self._versions_[0])

    def __getitem__(self, key):
        """
        Modular Retrieval
        """

        return self.entry[key]

    def __setitem__(self, key, point):
        # TODO Raise Error
        pass

    def __iter__(self):

        for item in list(self._versions_[0]):
            yield item

        raise StopIteration

    def __contains__(self, check):

        # only one item to check
        if isinstance(check, basestring) or isinstance(check, int) or callable(check) or isinstance(check, Setting):
            for item in self:
                if check == item:
                    return True

        try:
            # see if item being checked can even fit in instance
            len_check, len_self = len(check), len(self)

            def check_multiple(in_list):
                # checks tuples and lists
                try:
                    if len_check > len_self:
                        return False
                    for version in self.versions():
                        """
                        [1,2,3,4] -> [5,5,1,2,3,4]
                        i -> [0,1,2,3]
                        """
                        for i in range(len_self-(len_check-1)):
                            truth = True
                            for n in range(len_check):
                                truth = truth and (version[n+i] == in_list[n])
                            if truth:
                                return True
                # should catch dictionaries types
                #   except those that have numeric keys, start with 0 and are in order
                except KeyError:
                    return False

            if isinstance(check, Band):
                for _list_ in check.versions():
                    _return_ = check_multiple(_list_)
                    if _return_ is not None:
                        return _return_
            else:
                print(check)
                _return_ = check_multiple(check)
                if _return_ is not None:
                    return _return_

        except TypeError:
            return False

    def versions(self):

        for item in self._versions_:
            yield item

        raise StopIteration


class Ring(Band):

    def __init__(self, *items):
        Band.__init__(self, *items)

    # replaces Band's method
    def _get_versions_(self):
        versions = []
        for item in self.extrapolated:

            for i in range(len(item)):
                this = []
                for n in range(len(item)):

                    this.append(item[((n - i) % len(item))])

                versions.append(tuple(this))

        return versions

    def __getitem__(self, key):
        """
        Modular Retrieval
        """
        return self.entry[(key % len(self))]


class Loop(Band):

    def __init__(self, *items):
        Band.__init__(self, *items)

    def shift(self, amount):
        versions = []
        for item in self.versions():
            #print(item)
            this = []
            for i in range(len(item)):
                #print(i, ((amount + i) % len(item)))
                this.append(item[((amount + i ) % len(item))])

            versions.append(tuple(this))
        self._versions_ = versions

if __name__ == '__main__':
    pass

    #a = Ring('a', 'b')
    #b = Ring('a', 'p', 'p', 'p')
    c = Loop( Ring('n', 'o'), Ring('a', 'p'))

    print(c._versions_)
    c.shift(1)
    print(c._versions_)

    #print(c in Loop('o', 'p', 'p', 'a', 'p', 'o'))7777777777