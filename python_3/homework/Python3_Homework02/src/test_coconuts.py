'''

Created on 06/5/2015

@author: cbabilotte
'''

import unittest
from coconuts import Coconut
from coconuts import Inventory

class Test(unittest.TestCase):
    def setUp(self):
        self.south_asian = Coconut(coconut_type="South Asian", coconut_weight=3)
        self.middle_eastern = Coconut(coconut_type="Middle Eastern", coconut_weight=2.5)
        self.american = Coconut(coconut_type="American", coconut_weight=3.5)
        self.inventory = Inventory()
    
    def test_coconuts(self):
        '''
        Test to ensure that each coconut type have different weight
        '''
        self.assertNotEqual(self.south_asian, self.middle_eastern , "South Asian and Middle Eastern coconuts have the same weight")
        self.assertNotEqual(self.south_asian, self.american, "South Asian and American coconuts have the same weight")
        self.assertNotEqual(self.middle_eastern, self.american, "Middle Eastern and American coconuts have the same weight")
        
    def test_inventory_add_coconut(self):
        '''
        Test inventory add_coconut
        Raise AttributeError if it passes a string
        '''
        self.assertRaises(AttributeError, self.inventory.add_coconut, "Bermuda")
     
    def test_inventory_total_weight(self):
        '''
        Test to ensure that total weight calculation is correct
        '''
        # 2 South Asians
        self.inventory.add_coconut(self.south_asian)
        self.inventory.add_coconut(self.south_asian)
        
        # 1 Middle Easter
        self.inventory.add_coconut(self.middle_eastern)
        
        # 3 American
        self.inventory.add_coconut(self.american)
        self.inventory.add_coconut(self.american)
        self.inventory.add_coconut(self.american)
        
        observed = self.inventory.total_weight()
        expected = (self.south_asian.coconut_weight * 2) + (self.american.coconut_weight * 3) + (self.middle_eastern.coconut_weight)
        
        self.assertEqual(observed, expected)
        
        
if __name__ == "__main__":
    unittest.main()