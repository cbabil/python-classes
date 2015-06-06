import unittest
import Archives
import os
import zipfile
import shutil


class TestArchives(unittest.TestCase):

    def setUp(self):
        self.fnames = ["groucho", "harpo", "chico"]
        self.path = "v:\\workspace\\Archives_Homework\\src\\archive_me"

        # Make test files to compress
        if not (os.path.exists(self.path)):
            os.mkdir(self.path)
        for fn in self.fnames:
            f = open(os.path.join(self.path, fn), "w")
            f.close()

        # Make test subdirectory and subdirectory files
        if not (os.path.exists(self.path + "\\test")):
            os.mkdir(self.path + "\\test")
        for fn in self.fnames:
            f = open(os.path.join(self.path + "\\test", fn), "w")
            f.close()

        # Compress direcotry
        Archives.archivedir(self.path)

    def test_dirzip(self):
        ''' This test check to see if the zip file has been created '''

        if os.path.isfile(self.path + '.zip'):
            observed = self.path + '.zip'
        else:
            observed = None
        expected = self.path + ".zip"

        self.assertEqual(observed, expected)

    def test_dirzip_content(self):
        ''' 
        This test check the content of the zip file to make sure it
        only contains directories "groucho", "harpo", "chico
        '''

        zf = zipfile.ZipFile(self.path + '.zip', 'r')
        observed = zf.namelist()
        expected = [
            os.path.basename(self.path) + "/" + directory for directory in self.fnames]
        self.assertEqual(observed, expected)

    def tearDown(self):
        shutil.rmtree(self.path)
        os.remove(self.path + ".zip")

if __name__ == "__main__":
    unittest.main()
