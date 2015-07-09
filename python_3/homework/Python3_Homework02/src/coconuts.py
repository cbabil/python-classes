'''
Created on 06/05/2015

@author: cbabilotte
'''

class Coconut(object):
    '''
    A Coconut object
    '''
    def __init__(self, coconut_type, coconut_weight):
        '''
        Coconuts have type and weight
        '''
        self.coconut_type = coconut_type
        self.coconut_weight = coconut_weight
        
class Inventory(object):
    '''
    An inventory object for managing Coconuts
    '''
    def __init__(self):
        self.inventory = []

    def add_coconut(self, coconut):
        '''
        Add coconut to inventory
        Throw AttributError if argument is not a coconut object
        '''
        if not isinstance(coconut, Coconut):
            raise AttributeError("Must be a Coconut")
        self.inventory.append(coconut)
        
    
    def total_weight(self):
        '''
        Function to return total weights of coconuts
        '''
        total_weight = 0
        for coconut in self.inventory:
            total_weight += coconut.coconut_weight
        return total_weight