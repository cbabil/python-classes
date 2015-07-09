'''
functionfinder.py print all functions
and their arguments as they would appear
in a def statement.
'''

from inspect import getmembers, isfunction, getfullargspec, formatargspec
import os


class FuncFinder(object):

    '''
    A FuncFinder object
        func_lst    The list of functions from the module imported
    '''

    def __init__(self):
        self.func_lst = getmembers(os, isfunction)

    def get_funclst_argspec(self):
        '''
        Returns formatted arg
        for functions as generator
        '''
        func_specs = ('def {}{}'.format(
            func[0], formatargspec(*getfullargspec(func[1]))) for
            func in self.func_lst)
        return func_specs

if __name__ == "__main__":
    """
    Demonstrate how calling the get_funclst_argspec method on our
    class creates a generator capable of printing expected output.
    """

    for func in FuncFinder().get_funclst_argspec():
        print(func)
