'''
This module tests to see if a given function
returns a count of unique extension for a given directory
'''
import unittest
import shutil
import os
import FileHandling
import tempfile


class TestExtension(unittest.TestCase):

    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp()
        os.chdir(self.dirname)

    def test_1(self):
        '''
        This function creates sample files and
        tests the directory ext function 
        for a given file directory.
        '''

        # Create sample files
        self.file_exts = [
            'file.txt', 'file.doc', 'file.log', 'file.py', 'file1.txt']
        for fn in self.file_exts:
            fh = open(fn, 'w')
            fh.close()
        counts = FileHandling.count_fileext(self.dirname)
        expected_counts = {'.txt': 2, '.doc': 1, '.log': 1, '.py': 1}
        self.assertEqual(counts, expected_counts)

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)

if __name__ == "__main__":
    unittest.main()