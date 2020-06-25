import unittest
from extract_urls import extract_urls
import os

class TestExtract_Urls(unittest.TestCase):
    def test_basic(self):
        with open(r"C:\Users\Chris\Desktop\Python Scripts\extract_urls\test_dir\testfile.txt", 'r') as f:
            text = f.read().replace('\n', '')
            urls = extract_urls(text)
            print(urls)
            self.assertEqual(urls,
                             ["http://flash.lincolninteractive.com/ArtsAlive/third_theme/Unit1/Lesson1/Arts_Alive_th3_U1L1.swf",
                              "https://artsaliverepo.s3.amazonaws.com/Arts_Alive/third_theme/Unit1/Lesson1/arts_alive_jr3_U1L1_Pic1.jpg"])

if __name__ == '__main__':
    unittest.main()
