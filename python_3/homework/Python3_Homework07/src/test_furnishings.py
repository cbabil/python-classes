'''
Created on June 13 2015

@author: cbabilotte
'''
import unittest
from furnishings import *

class Test(unittest.TestCase):

    def test_map_the_home(self):
        '''
        Test map_the_home function
        returns a dictionary
        '''
        home = []
        bed = Bed('Bedroom')
        sofa = Sofa('Living Room')
        home.append(bed)
        home.append(sofa)
        map_home = map_the_home(home)
        
        expected = {bed.room: [bed], sofa.room: [sofa]}
        observed = map_home
        self.assertDictEqual(expected, observed)
    
    def test_counter(self):
        '''
        Test counter function
        returns object and count for each objects
        '''
        home = []
        home.append(Bed('Bedroom'))
        home.append(Sofa('Living Room'))
        observed = counter(home)
        expected = "Beds: 1" +"\n"+ "Sofas: 1"
        self.assertEqual(expected, observed)     
        
if __name__ == "__main__":
    unittest.main()