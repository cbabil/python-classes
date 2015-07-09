'''
A subclass of the standard dict class
used to display alternative
exception handling behavior.
'''


class DictDefault(dict):

    def __init__(self, default):
        dict.__init__(self)
        self.default = default

    def __getitem__(self, key):
        ''' returns default value on key error '''
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.default