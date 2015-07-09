
'''
ctxmgr.py: A context manager class that suppresses
any ValueError exceptions that occur in the controlled
suite, but allows any other exception to be raised in the 
surrounding context.
'''

from contextlib import contextmanager
@contextmanager
def context():
    try:
        yield
    except ValueError:
        "suppress any ValueError exceptions"
        pass
    except:
        "raise other exceptions"
        raise
    finally:
        pass

if __name__ == '__main__':
    with context() as cm:
        ''' ValueError exception is suppressed '''
        x = int('one')
    
    with context() as cm:
        ''' Any other exception is raised '''
        x = 1 / 0