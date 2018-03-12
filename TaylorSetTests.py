import unittest

from TaylorSet import TaylorSet

class MaximumTestCaseOne(unittest.TestCase):
    def test_basic(self):
        my_data = [ 1, 2, 3, 4, 5 ]
        my_set = TaylorSet(my_data)
        self.assertEqual(my_set.average(), 3)

unittest.main()
