'''
Class-based dict allowing tuple subscripting & sparse data

Created on July 01 2015
'''


class array:

    def __init__(self, X, Y, Z):
        "Create a MxNxL 3D-array using dict"
        self._data = {}
        self._xsize = X
        self._ysize = Y
        self._zsize = Z

    def __getitem__(self, key):
        "Returns the appropriate element for a three-element subscript tuple."
        x, y, z = self._validate_key(key)
        try:
            return self._data[x, y, z]
        except KeyError:
            return 0

    def __setitem__(self, key, value):
        "Sets the appropriate element for a three-element subscript tuple"
        x, y, z = self._validate_key(key)
        self._data[x, y, z] = value

    def _validate_key(self, key):
        """Validate a key against the array's shape, returning good tuples.
        Raises KeyError on problems."""
        x, y, z = key
        if (x in range(self._xsize) and y in range(self._ysize)
                and z in range(self._zsize)):
            return key
        raise KeyError("Subscript out of range")