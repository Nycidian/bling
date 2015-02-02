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


class Band(object):

    def __init__(self, *items):
        self._items = tuple(items)
        self._versions_ = self._get_versions_()
        self._hash_ = self._make_hash_()

    def _get_versions_(self):
        return [self._items]

    def _make_hash_(self):

        this = []
        for i in range(len(self._items)):

            string = self.__class__.__name__
            for n in range(len(self._items)):
                string += str(hash(self[((n - i) % len(self))]))
            this.append(string)

        return hash(self.__class__.__name__ + max(this))

    def __hash__(self):
        return self._hash_

    def __eq__(self, other):
        try:
            return hash(self) == hash(other)
        except TypeError:
            return False

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
        return self._items[key]

    def __setitem__(self, key, point):
        # TODO Raise Error
        pass

    def __iter__(self):

        for item in list(self._items):
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
        for i in range(len(self._items)):
            items = []
            for n in range(len(self._items)):
                item = self[n - i]
                items.append(item)

            versions.append(tuple(items))

        return versions


    def __getitem__(self, key):
        """
        Modular Retrieval
        """
        return self._items[(key % len(self))]

    def cycle(self):
        items = list(self._items)
        if len(self) > 1:
            items += items[:-1]

        for item in items:
            yield item

        raise StopIteration


class Loop(Band):

    def __init__(self, *items):
        Band.__init__(self, *items)

    def _make_hash_(self):

        string = self.__class__.__name__

        for item in self._items:
            string += str(hash(item))
            
        return hash(string)


if __name__ == '__main__':
    pass

    l = Loop('a', 'b')
    L = Loop('b', 'a')

    print(hash(l), hash(L))