import unittest
from ccwc import countBytes, countLines, countWords, countCharacters, readfile

class Test(unittest.TestCase):
    def setUp(self):
        self.file = readfile("./super-test.txt")

    def tearDown(self):
        self.file.close()

    def test_count_bytes(self):
        self.assertEqual(countBytes(self.file), 120)

    def test_count_lines(self):
        self.assertEqual(countLines(self.file), 10)

    def test_count_words(self):
        self.assertEqual(countWords(self.file), 20)

    def test_count_characters(self):
        self.assertEqual(countCharacters(self.file), 120)

if __name__ == '__main__':
    unittest.main()




