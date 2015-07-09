'''
composable.py: defines a composable function class

Created on June 30th 2015
'''

import types

class Composable:
    
    def __init__(self, f):
        "Store reference to proxied function."
        self.func = f
    
    def __call__(self, *args, **kwargs):
        "Proxy the function, passing all arguments through."
        return self.func(*args, **kwargs)
    
    def __mul__(self, other):
        "Return the composition of proxied and another function."
        if type(other) is Composable:
            def anon(x):
                return self.func(other.func(x))
            return Composable(anon)
        elif type(other) is types.FunctionType:
            def anon(x):
                return self.func(other(x))
            return Composable(anon)
        raise TypeError("Illegal operands for multiplication")
    
    def __pow__(self, n):
        "Return the n-th power of the function"
        if not isinstance(n, int):
            raise TypeError("n must be an integer.")
        if n <= 0:
            raise ValueError("n must be a positive integer.")
        res = self.func
        for _ in range(1, n):
            res = self.__mul__(res)
        return res
   
    def __rep__(self):
        return "<Composable function {0} at 0x{1:X]>".format(self.func.__name__, id(self))