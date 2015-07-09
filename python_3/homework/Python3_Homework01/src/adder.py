'''
Function to accept two arguments,
and add them together. Raise a TypError if objects
are not of integer types
'''

def adder(obj_1, obj_2):
    '''Validates arguments as integer and add together.'''
    if isinstance(obj_1, int) and isinstance(obj_2, int):
        return obj_1 + obj_2
    else:
        raise TypeError('Not an integer')