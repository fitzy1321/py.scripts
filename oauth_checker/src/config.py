"""
Configuration Manager class.

Gets data from json file and loads it into dictionary.
Config class should behave just like a dict object because
it inherits from dict.
"""

import atexit  # for object cleanup

import orjson


class ConfigManager(dict):
    """Configuration Manager Class."""

    __hasAltered__ = False
    __datafile__ = "app.data.json"
    __datadict__ = dict()

    def __init__(self):
        """Is Constructor Method."""
        # Read in json data from json file into class dict
        self.__readfile__()
        # Can't use 'open' in __del__ method, uing atexit instead
        atexit.register(self.__cleanup__)

    def __readfile__(self):
        """Read json data from __datafile__."""
        with open(self.__datafile__, "r") as datafile:
            # main method will catch FileNotFound exception
            self.__datadict__ = orjson.loads(datafile.read())

    def __cleanup__(self):
        """__cleanup method replaces __del__ dunder method."""
        if self.__hasAltered__:
            with open(self.__datafile__, "w") as f:
                f.write(
                    orjson.dumps(
                        self.__datadict__,
                        option=orjson.OPT_INDENT_2,
                    ).decode("utf-8")
                )

    def __setitem__(self, key, item):
        """See dunder method docs for info on '__setitem__' method."""
        self.__datadict__[key] = item
        self.__hasAltered__ = True

    def __getitem__(self, key):
        """See dunder method docs for info on '__getitem__' method."""
        return self.__datadict__[key]

    def __repr__(self):
        """See dunder method docs for info on '__repr__' method."""
        return repr(self.__datadict__)

    def __delitem__(self, key):
        """See dunder method docs for info on __delitem__ method."""
        del self.__datadict__[key]

    def clear(self):
        """See Dict docs for info on clear method."""
        return self.__datadict__.clear()

    def copy(self):
        """See Dict docs for info on copy method."""
        return self.__datadict__.copy()

    def has_key(self, k):
        """See Dict docs for info on copy method."""
        return k in self.__datadict__

    def update(self, *args, **kwargs):
        """See Dict docs for info on copy method."""
        return self.__datadict__.update(*args, **kwargs)

    def keys(self):
        """See Dict docs for info on copy method."""
        return self.__datadict__.keys()

    def values(self):
        """See Dict docs for info on copy method."""
        return self.__datadict__.values()

    def items(self):
        """See Dict docs for info on copy method."""
        return self.__datadict__.items()

    def pop(self, *args):
        """See Dict docs for info on copy method."""
        return self.__datadict__.pop(*args)

    def __contains__(self, item):
        """See dunder methods docs for info on '__contains__' method."""
        return item in self.__datadict__

    def __iter__(self):
        """See dunder method docs for info on '__iter__' method."""
        return iter(self.__datadict__)
