'''
A simple alphabet iterator
'''

def alphabator(lst):
    ''' Decimal to Ascii Character conversion '''
    for dec in lst:
        if dec in range(1,27):
            yield chr(dec+64)
        else:
            yield dec
        
    