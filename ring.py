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
        self._versions_ = []
        self._hash_ = self._make_hash_()

    def _make_hash_(self):

        string = self.__class__.__name__
        items = []
        for i in range(len(self._items)):
            item = self[i]
            items.append(item)
            string += str(hash(item))

        self._versions_.append(items)

        return hash(string)

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
        # TODO add function that checks if a single object is in or if a tuple of objects is contained within in order
        if isinstance(check, basestring) or isinstance(check, int) or callable(check) or isinstance(check, Setting):
            for item in self:
                if check == item:
                    return True

        try:
            # see if item being checked can even fit in ring
            self_len, check_len = len(self), len(check)
            if check_len > self_len:
                return False

            def check_multiple(in_list, in_len, r, r_len):
                # checks tuples and lists
                try:
                    for i in range(r_len):
                        truth = True
                        for n in range(in_len):
                            truth = truth and (r[n+i] == in_list[n])
                        if truth:
                            return True
                # should catch dictionaries types
                #   except those that have numeric keys, start with 0 and are in order
                except KeyError:
                    return False

            if isinstance(check, Ring):
                for lst in check.versions():
                    _return_ = check_multiple(lst, check_len, self, self_len)
                    if _return_ is not None:
                        return _return_
            else:
                _return_ = check_multiple(check, check_len, self, self_len)
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
    def _make_hash_(self):
        this = []
        for i in range(len(self._items)):
            items = []
            string = self.__class__.__name__
            for n in range(len(self._items)):
                item = self[n - i]
                items.append(item)
                string += str(hash(item))
            this.append(string)
            self._versions_.append(items)

        return hash(max(this))

    # replaces Band's method
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


if __name__ == '__main__':

    a = 1
    b = []

    def func():
        a=1

    set = Setting('o', 'a')
    ring = [set, 'a', set]
    ring2 = Ring('o', 'o', 'a', 'p', 'n')
    ring3 = Loop('o', 'o', 'a', 'p', 'n')

    for i in ring3.versions():
        print(i)

    print(hash(ring2), hash(ring3))

