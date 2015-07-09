'''

Created on June 14 2015

@author: cbabilotte
'''

class Centipede(object):
    
    def __init__(self):
        ''' Initialize empty list '''
        self.__dict__['stomach'] = []
        self.__dict__['legs'] = []
    
    def __str__(self):
        ''' Returns the content of the stomach '''
        return ','.join(self.stomach)
    
    def __call__(self, *args):
        self.__dict__['stomach'].extend(args)
    
    def __setattr__(self, key, value):
        '''
        Protect the 'legs' and 'stomach' attributes against 
        having their values reset from outside
        '''
        if key in ('stomach', 'legs'):
            raise AttributeError("{0} is for internal use only".format(key))
        self.legs.extend([key])
        self.__dict__[key] = value
    
    def __repr__(self):
        ''' Returns the content of the legs '''
        return ",".join(self.legs)