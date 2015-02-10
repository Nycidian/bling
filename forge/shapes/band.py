__author__ = 'Nycidian'


class Band(object):
    """
    Cyclic Method
    """
    def __init__(self):
        pass

    def _get_versions_(self):
        versions = []
        for item in self._versions_:

            for i in range(len(item)):
                this = []
                for n in range(len(item)):

                    this.append(item[((n - i) % len(item))])

                versions.append(tuple(this))

        return versions
