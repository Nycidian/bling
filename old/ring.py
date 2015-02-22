__author__ = 'Nycidian'

# basestring for python 3
try:
    basestring
except NameError:
    basestring = str

    """
class Charm(object):
    '''
    Container that evaluates to true if any one of the contents is equal to what it's tested against
    '''

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


class Iterable(object):

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

        return self._items[(key % len(self))]

    def __str__(self):
        return '{}{}'.format(self.__class__.__name__, self._items)

    def __repr__(self):
        return '{}{}'.format(self.__class__.__name__, self._items)

    def __len__(self):
        return len(self._items)

    """

class Wire(object):

    def __init__(self, *items):
        self.entry = tuple(items)
        self.extrapolated = self._extrapolate_([items])
        self.versions = self._get_versions_()
        self._hash_ = self._make_hash_()

    @staticmethod
    def wired(this):
        """
        :param this: list of iterable objects
        :return: Returns True if any return of an iterable is a Wire class
        """
        if len(this) == 0:
            return False
        for item in this:
            for i in item:
                if isinstance(i, Wire):
                    return True
        return False

    def _extrapolate_(self, object_instance):
        _return_ = []
        while len(object_instance) > 0:
            work = object_instance.pop()
            end = len(work)
            for n in range(end):
                if isinstance(work[n], Wire):

                    for version in work[n].versions:
                        object_instance.append(
                            list(work[:n]) + list(version) + list(work[n+1:]))
                    break
                if n == (end - 1):
                    _return_.append(work)

        non_duplicate = set()
        if self.__class__.__name__ == 'Ring':
            # Ring Class
            for item in _return_:
                non_duplicate.add(Cast(*item))
        else:
            for item in _return_:
                non_duplicate.add(tuple(item))
        _return_ = list(non_duplicate)

        return _return_


    def _get_versions_(self):
        return self.extrapolated

    def _make_hash_(self):
        print(self.versions)
        this = []
        for version in self.versions:
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
        return '{}({})'.format(self.__class__.__name__, self.entry)

    def __repr__(self):
        return '{}{}'.format(self.__class__.__name__, self.entry)

    @staticmethod
    def __bool__():
        return True

    def __nonzero__(self):      # Python 2 compatibility
        return type(self).__bool__(self)

    def __len__(self):
        return len(self.versions[0])

    def __getitem__(self, key):
        """
        Modular Retrieval
        """

        return self.entry[key]

    def __setitem__(self, key, point):
        # TODO Raise Error
        pass

    def __iter__(self):

        for item in list(self.versions[0]):
            yield item

        raise StopIteration

    def __contains__(self, other):

        # only one item to check
        if isinstance(other, basestring) or isinstance(other, int) or callable(other) or isinstance(other, Charm):
            for item in self:
                if other == item:
                    return True

        try:
            # see if item being checked can even fit in instance
            len_other, len_self = len(other), len(self)
            def check_multiple(in_list):
                # checks tuples and lists
                try:
                    if len_other > len_self:
                        return False
                    for version in self.versions:
                        """
                        [1,2,3,4] -> [5,5,1,2,3,4]
                        i -> [0,1,2,3]
                        """
                        for i in range(len_self-(len_other-1)):
                            truth = True
                            for n in range(len_other):
                                truth = truth and (version[n+i] == in_list[n])
                            if truth:
                                return True
                # should catch dictionaries types
                #   except those that have numeric keys, start with 0 and are in order
                except KeyError:
                    return False

            if isinstance(other, Wire):
                for _list_ in other.versions:
                    _return_ = check_multiple(_list_)
                    if _return_:
                        return _return_
            else:
                _return_ = check_multiple(other)
                if _return_:
                    return _return_

        except TypeError:
            return False

        return False

    def out_of(self, other):

        # only one item to check, make sure this class len is 1
        if isinstance(other, basestring) or isinstance(other, int) or callable(other) or isinstance(other, Charm):
            if len(self) == 1:
                if other == self[0]:
                    return True

        try:
            len_other, len_self = len(other), len(self)
            # see if item being checked can even fit in instance
            if len_other < len_self:
                return False

            def check_multiple(in_list):
                # checks tuples and lists
                try:
                    for version in self.versions:
                        """
                        [1,2,3,4] -> [5,5,1,2,3,4]
                        i -> [0,1,2,3]
                        """
                        for i in range(len_other-(len_self-1)):
                            truth = True
                            for n in range(len_self):
                                truth = truth and (version[n] == in_list[n+i])
                            if truth:
                                return True

                # should catch dictionaries types
                #   except those that have numeric keys, start with 0 and are in order
                except KeyError:
                    return False

            if isinstance(other, Wire):
                for item in other.versions:
                    _return_ = check_multiple(item)
                    if _return_:
                        return _return_
            else:
                _return_ = check_multiple(other)
                if _return_:
                    return _return_

        except TypeError:
            return False

        return False

    def versions(self):

        for item in self.versions:
            yield item

        raise StopIteration


class Ring(Wire):

    def __init__(self, *items):
        Wire.__init__(self, *items)

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


class Chain(Wire):

    def __init__(self, *items):
        Wire.__init__(self, *items)

    def shift(self, amount):
        versions = []
        for item in self.versions:
            this = []
            for i in range(len(item)):
                this.append(item[((i - amount) % len(item))])

            versions.append(tuple(this))
        self.versions = versions
        self._hash_ = self._make_hash_()
        return self


class Locket(Wire):
    """
    Container that hold multiple objects but only return one instance at a time
    """

    def __init__(self, *items):
        self.entry = tuple(items)
        self.extrapolated = self._extrapolate_([[t] for t in items])
        self.versions = self._get_versions_()
        self._hash_ = self._make_hash_()

    def shift(self, amount):
        versions = []
        for item in self.versions:
            this = []
            for i in range(len(item)):
                this.append(item[((i - amount) % len(item))])

            versions.append(tuple(this))
        self.versions = versions
        self._hash_ = self._make_hash_()
        return self


if __name__ == '__main__':

    a = Locket('http://www.','https://www.')
    b = Locket('google', 'yahoo', 'duckduckgo')
    c = Locket('.com', '.co', '.in')
    loop_test = Chain(a,b,c)

    #print(loop_test.versions)
    for t in loop_test.versions:
        print(''.join(t))
