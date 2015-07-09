"""
Tests to verify message creation and storage. 
Also performs profiling of these operations.
"""

import mysql.connector
from database import login_info
import jokes
import messages
import emailgenerator
import settings
import unittest

class TestEmail(unittest.TestCase):

    def setUp(self):
        '''
        Define db handler and different tables
        '''
        self.db = mysql.connector.Connect(**login_info)
        self.cursor = self.db.cursor()

        # Database: joke
        self.jotd_tbl = 'jotd'
        self.jotd_file = "jokes.txt"
        self.startdate = settings.STARTTIME

        # Database: message
        self.email_tbl = 'message' 
        self.daycount = settings.DAYCOUNT
        self.recipients = settings.RECIPIENTS
        
    def test_create_db_jokes(self):
        '''
        Creation of jokes database
        '''

        # We drop the table if exists
        observed = jokes.drop(self.cursor, self.jotd_tbl)
        expected = "Droping table jotd: OK"
        self.assertEqual(observed, expected)

        # We create the table
        observed = jokes.create(self.cursor, self.jotd_tbl)
        expected = "Creating table jotd: OK"
        self.assertEqual(observed, expected)

        # Insert jokes data
        observed = jokes.insert(
            self.cursor, self.jotd_file, self.jotd_tbl)
        expected = "Insert table jotd: OK"
        self.assertEqual(observed, expected)

        # Retrieve joke
        observed = jokes.retrieve(
            self.cursor, self.jotd_tbl)

        expected = ""
        with open("jokes.txt") as file:
            for line in file.readlines():
                line = line.rstrip()
                if line == observed:
                    expected = line
        
        self.assertEqual(observed, expected, "Joke in Database is not found in joke file")

    def test_create_db_message(self):
        '''
        Creation of message database
        '''
        
        # We drop the table if exists
        observed = messages.drop(self.cursor, self.email_tbl)
        expected = "Droping table message: OK"
        self.assertEqual(observed, expected)

        # We create the table
        observed = messages.create(self.cursor, self.email_tbl)
        expected = "Creating table message: OK"
        self.assertEqual(observed, expected)

    def test_create_email(self):
        '''
        This test generation of email
        '''
        tbl = "message"
        
        # Build the jokes database
        jokes.drop(self.cursor, self.jotd_tbl)
        jokes.create(self.cursor, self.jotd_tbl)
        jokes.insert(
            self.cursor, self.jotd_file, self.jotd_tbl)
        
        emailgenerator.create_email(self.cursor, settings.SENDER, settings.RECIPIENTS, settings.STARTTIME, settings.DAYCOUNT, tbl)
        
        observedCount = len(messages.retrieveall(
            self.cursor, tbl))
    
        expectedCount = len(settings.RECIPIENTS) * settings.DAYCOUNT
        self.assertEqual(expectedCount, observedCount, "Unexpected number of messages created")

    
    def tearDown(self):
        self.db.close()
    
if __name__ == "__main__":
    unittest.main()