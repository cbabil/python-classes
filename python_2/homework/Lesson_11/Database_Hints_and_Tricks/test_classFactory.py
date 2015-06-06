import unittest
from classFactory import build_row

class DBTest(unittest.TestCase):
    
    def setUp(self):
        import mysql.connector
        from database import login_info
        self.db = mysql.connector.Connect(**login_info)
        self.cursor = self.db.cursor()


    def test_retrieve_single_record(self):
                
        C = build_row('animal', 'id', 'name', 'family', 'weight', curs=self.cursor, condition="name='Ellie'")
        observed = [data for data in C.retrieve(C, curs=self.cursor, condition="name='Ellie'")]
        expected = "[animal_record(1, 'Ellie', 'Elephant', 2350)]"
        self.assertEqual(str(observed), expected)

    def test_retrieve_multple_records(self):

        C = build_row("animal", "id",  "name", "family", "weight", curs = self.cursor, condition="family='Snake'")
        observed = [data for data in C.retrieve(C, curs = self.cursor, condition="family='Snake'")]
        expected = "[animal_record(5, 'Sam', 'Snake', 24), animal_record(6, 'Steve', 'Snake', 35)]"
        self.assertEqual(str(observed), expected)

    def test_retrieve_no_record(self):
    
        C = build_row("animal", "id",  "name", "family", "weight", curs = self.cursor, condition="name='None'")
        observed = [data for data in C.retrieve(C, curs = self.cursor, condition="name='None'")]
        expected = "[]"
        self.assertEqual(str(observed), expected)
        
    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()