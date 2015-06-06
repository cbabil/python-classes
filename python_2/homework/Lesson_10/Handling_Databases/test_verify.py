import unittest
from verify import verify_animal


class AnimalTest(unittest.TestCase):

    def setUp(self):
        import mysql.connector
        from database import login_info
        self.db = mysql.connector.Connect(**login_info)

    def test_verify_animal(self):
        from addtables import drop_table
        from addtables import create_animal
        from addtables import create_food
        
        # First we setup the tables with data
        table = ['food', 'animal']
        drop_table(self.db, table)
        create_animal(self.db)
        create_food(self.db)
    
        observed = verify_animal(self.db)
        expected = []
        self.assertEqual(observed, expected)
        
    def test_verify_animal_nofood(self):
        
        from addtables_nofood import drop_table
        from addtables_nofood import create_animal
        from addtables_nofood import create_food
        
        # First we setup the tables with data
        table = ['food', 'animal']
        drop_table(self.db, table)
        create_animal(self.db)
        create_food(self.db)
        
        observed = verify_animal(self.db)
        expected = [(8,'NoFood', 'Tiger', 350)]
        self.assertEqual(observed, expected)
        
    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()