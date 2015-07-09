'''
Decorator to take argument and
add it as the first argument to all calls to 
decorated functions.
'''
from functools import wraps

def addarg(arg):
    '''
    Returns a decorator that adds an argument 
    as the first argument to a decorated function.
    '''
    def decorator(f):
        '''
        Decorate a function to add argument as first
        argument to decorated function.
        '''
        @wraps(f)
        def wrapper(*args, **kwargs):
            '''
            Adds an arg to the list of args if provided
            '''
            return f(arg, *args, **kwargs)
        return wrapper
    return decorator