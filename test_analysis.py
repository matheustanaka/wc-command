import unittest
from ccwc import countBytes, countLines, countWords, countCharacters

class Test(unittest.TestCase):
    def test_count_lines(self):
        file = "./super-test.txt" 
        self.assertEqual(countLines(file), 3)

if __name__ == '__main__':
    unittest.main()




