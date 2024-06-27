import unittest
from Mathematics import Mathematics

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.math = Mathematics()
    def test_sum(self):
        result = self.math.sumTwoNumbers(10,5)
        self.assertEqual(result, 15)  # add assertion here
    def test_multiply(self):
        self.assertEqual(5,5)

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()
