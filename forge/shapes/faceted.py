__author__ = 'Nycidian'


class Faceted(object):

    @staticmethod
    def _len_():
        return 1

    def _get_versions_(self):
        versions = []
        for item in self._versions_:
            for i in range(len(item)):
                versions.append(item[i])

        return versions