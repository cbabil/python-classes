import os
import emailgenerator
import unittest


class emailTest(unittest.TestCase):

    def setUp(self):
        self.path = str(os.getcwd())

    def test_email_txt(self):
        attach_txt = self.path + "\\" + "sample.txt"
        attachments = [attach_txt]
        msg = emailgenerator.generate_email("you@you.com", "Email body.", attachments)
        lst = []
        for part in msg.walk():
            lst.append(part.get_content_type())

        self.assertEqual(lst, ['multipart/mixed', 'text/plain', 'text/plain'],
                         "Email with only text was not correctly formed")

    def test_email_image(self):
        attach_png = self.path + "\\" + "python-logo.png"
        attachments = [attach_png]
        msg = emailgenerator.generate_email("you@you.com", "Email body.", attachments)
        lst = []
        for part in msg.walk():
            lst.append(part.get_content_type())

        self.assertEqual(lst, ['multipart/mixed', 'text/plain', 'image/png'],
                         "Email with image was not correctly formed")

    def test_email_other(self):
        attach_txt = self.path + "\\" + "sample.xxx"
        attachments = [attach_txt]
        msg = emailgenerator.generate_email("you@you.com", "Email body.", attachments)
        lst = []
        for part in msg.walk():
            lst.append(part.get_content_type())

        self.assertEqual(lst, ['multipart/mixed', 'text/plain',
                               'application/octet-stream'], "Email with 'other' was not correctly formed")

if __name__ == "__main__":
    unittest.main()
