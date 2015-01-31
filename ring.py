__author__ = 'Nycidian'


class Ring(object):

    def __init__(self, *items):
        self._items = tuple(items)
        self._versions_ = []

        self._hash_ = self._make_hash_()

    def _make_hash_(self):
        this = []
        for i in range(len(self._items)):
            items = []
            string = ''
            for n in range(len(self._items)):
                item = self._items[((n - i) % len(self._items))]
                items.append(item)
                string += str(hash(item))
            this.append(string)
            self._versions_.append(items)

        return hash(max(this))

    def __eq__(self, other):
        try:
            return hash(self) == hash(other)
        except TypeError:
            return False

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

        for item in list(self._items):
            yield item

        raise StopIteration

    def cycle(self):
        items = list(self._items)
        if len(self) > 1:
            items += items[:-1]

        for item in items:
            yield item

        raise StopIteration

    def versions(self):

        for item in self._versions_:
            yield item

        raise StopIteration

    def __contains__(self, check):
        # TODO add function that checks if a single object is in or if a tuple of objects is contained within in order
        if isinstance(check, basestring) or isinstance(check, int) or callable(check):
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

if __name__ == '__main__':

    a = 1
    b = []

    def func():
        a=1

    ring = [(2, func), 'a']
    ring2 = Ring((2, func), 1, 'a', func, 4)

    print(ring in ring2)

