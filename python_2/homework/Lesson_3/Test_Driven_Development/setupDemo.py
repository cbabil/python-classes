"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""
import unittest
import tempfile
import shutil
import glob
import os


class FileTest(unittest.TestCase):

    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)

    def test_1(self):
        "Verify creation of files is possible"

        filelist = []
        for filename in ("this.txt", "that.txt", "the_other.txt"):
            f = open(filename, "w")
            f.write("Some text\n")
            filelist.append(filename)
            f.close()
            self.assertTrue(f.closed)

        self.assertEqual(os.listdir(self.dirname).sort(),
                         filelist.sort(), "Directory contains other files")

    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")

    def test_3(self):
        """Create a Binary file that contains exactly a million bytes"""

        fname = "mbytes.txt"
        nbytes = 1000000
        fh = open(fname, 'wb')
        fh.write(bytes(nbytes))
        fh.close()
        self.assertTrue(fh.closed)

        # Get the file stats
        fileinfo = os.stat(fname)
        print(fileinfo.st_size)
        self.assertEqual(nbytes, fileinfo.st_size, "Unexpected file size")

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)

if __name__ == "__main__":
    unittest.main()
