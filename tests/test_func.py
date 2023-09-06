import unittest
from funcs import func

class Test(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(func.sum(2,3), 5)

    def test_sub(self):
        self.assertEqual(func.sub(3,2), 1)

if __name__ == "__main__":
    unittest.main()